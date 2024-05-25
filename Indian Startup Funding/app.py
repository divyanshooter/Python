import streamlit as st
import pandas as pd

df=pd.read_csv("startup_funding.csv")

st.sidebar.title("Indian Startups")

user_selection=st.sidebar.selectbox("Select Analysis",["Overall","Startup","Investors"])

if user_selection=="Overall":
   st.title("Overall")

if user_selection=="Startup":
    st.title("Startup")
    startup_selection=st.sidebar.selectbox("Select Startup",df['Startup Name'].unique())

elif user_selection=="Investors":
    st.title("Investors")
    Investors_selection=st.sidebar.selectbox("Select Investor",df['Investors Name'].unique())