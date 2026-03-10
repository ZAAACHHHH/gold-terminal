import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")

st.title("Gold Intelligence Dashboard")

gold = yf.download("GC=F", period="5d", interval="1h")
dxy = yf.download("DX-Y.NYB", period="5d", interval="1h")
usdjpy = yf.download("JPY=X", period="5d", interval="1h")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Gold")
    st.line_chart(gold["Close"])

with col2:
    st.subheader("DXY")
    st.line_chart(dxy["Close"])

with col3:
    st.subheader("USDJPY")
    st.line_chart(usdjpy["Close"])

st.subheader("Current Prices")

st.write("Gold:", round(gold["Close"].iloc[-1],2))
st.write("DXY:", round(dxy["Close"].iloc[-1],2))
st.write("USDJPY:", round(usdjpy["Close"].iloc[-1],2))
