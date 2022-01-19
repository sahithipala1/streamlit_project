import yfinance as yf
import streamlit as st

st.write(""" 
# Simple Stock price App

shown are the stock closing price and volume of google!

""")

ticker_symbol = 'GOOGL'

ticker_Data = yf.Ticker(ticker_symbol)

ticker_Df = ticker_Data.history(period="id", start='2010-5-31', end="2022-5-31")

print(ticker_Df)
st.write("""

## Closing Price

""")
st.line_chart(ticker_Df.Close)

st.write("""
## Volume Price

""")
st.line_chart(ticker_Df.Volume)

