import streamlit as st
import pandas as pd
import yfinance as yf


st.write("""

# Us Population 


""")

df = pd.read_csv("p1-US-Cities-Population.csv")
data = yf.Ticker()
print(df.head())

