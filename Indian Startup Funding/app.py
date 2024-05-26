import streamlit as st
import pandas as pd
from database import Database

db=Database()

df=db.df


st.sidebar.title("Indian Startups")

user_selection=st.sidebar.selectbox("Select Analysis",["Overall","Startup","Investors"])

if user_selection=="Overall":
   st.title("Overall")

if user_selection=="Startup":
    st.title("Startup")
    startup_selection=st.sidebar.selectbox("Select Startup",sorted(df['startupname'].unique()))
    startup_btn=st.sidebar.button("Find Startup Details")

elif user_selection=="Investors":
    st.title("Investors")
    Investors_selection=st.sidebar.selectbox("Select Investor",sorted(set(df['investor'].str.split(',').sum())))
    startup_btn=st.sidebar.button("Find Investor Details")