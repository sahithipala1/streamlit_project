import streamlit as st
import pandas as pd
import base64
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

st.title("NBA Player State Explorer")

st.markdown(
    """
  This app performs simple webscraping of NBA player stats data!
  * **Python Libraries: base64, pandas, streamlit
  * **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
   
"""
)

st.sidebar.header("User Input Feature")
selected_year = st.sidebar.selectbox("Year :", list(reversed(range(1950, 2022))))


# Web scraping of NBA player stats:

@st.cache
def load_data(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_" + str(year) + " _per_game.html"
    l= pd.read_html(url, header=0)
    df =l[0]
    raw = df.drop(df[df.Age == "Age"].index)  # Deletes repeating headers in the content

    # Set the type column to str to address issues like below.
    # streamlit.errors.StreamlitAPIException: (
    # "Expected bytes, got of  int object", conversion failed for column FG% with type object)

    raw = raw.astype(str)
    raw = raw.fillna(0)

    play = raw.drop(["Rk"], axis=1)
    return play


player_stats = load_data(selected_year)

# sidebar - Team selection
sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect("Team", sorted_unique_team, sorted_unique_team)

unique_pos = ["C", "PF", "SF", "PG", "SG"]
selected_pos = st.sidebar.multiselect("position", unique_pos, unique_pos)

df_selected_team = player_stats[
    (player_stats.Tm.isin(selected_team)) & (player_stats.pos.isin(selected_pos))
    ]

st.header("Display player stats of Selected Team(s)")
st.write(
    "Data Dimension:"
    + str(df_selected_team.shape[0])
    + "rows and"
    + str(df_selected_team.shape[1])
    + "columns."

)

df_selected_team = df_selected_team.astype(str)
st.dataframe(df_selected_team)


def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="player stats.csv">Download CSV File</a>'
    return href


st.markdown(file_download(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button("Inter correlation Heatmap"):
    st.header("Inter correlation Matrix Heatmap")
    df_selected_team.to_csv("output.csv", index=False)
    df = pd.read_csv("output.csv")

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)
