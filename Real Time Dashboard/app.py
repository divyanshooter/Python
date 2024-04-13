import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import time

df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_icon=":bank:",
    page_title="Bank",
    layout="wide"
)

st.title(":bank: Live Data Bank Dashboard")

st.write(df)
col1,col2 = st.columns(2)
with col1:
    job=st.selectbox("Job",df["job"].unique())

with col2:
    minAge=df["age"].min()
    maxAge=df["age"].max()
    age=st.slider("Age",min_value=minAge,max_value=maxAge, value=  (minAge,maxAge))
    st.write(age)
