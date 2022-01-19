import streamlit as st
import pandas as pd

st.header("""
# basketball teams
""")

d = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2021_per_game.html")

print(len(d))

df = d[0]
print(df)