import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
# Simple Stock price App

shown are the stock closing price and volume of google!

""")

ticker_symbol = 'GOOGL'

ticker_Data = yf.Ticker(ticker_symbol)

ticker_Df = ticker_Data.history(period="id", start='2010-5-31', end="2022-5-31")

st.line_chart(ticker_Df.close)
st.line_chart(ticker_Df.volume)