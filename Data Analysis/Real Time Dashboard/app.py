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

#st.write(df)

col1,col2 = st.columns(2)
with col1:
    job=st.selectbox("Job",df["job"].unique())

with col2:
    minAge=df["age"].min()
    maxAge=df["age"].max()
    age=st.slider("Age",min_value=minAge,max_value=maxAge, value=  (minAge,maxAge))
    st.write(age)

placeholder=st.empty()

filtered_df=df[df["job"]==job]

for seconds in range(200):
   filtered_df["age_new"]=filtered_df["age"]*np.random.choice((1,5))
   filtered_df["balance_new"]=filtered_df["balance"]*np.random.choice((1,5))
   
   avg_age=filtered_df["age_new"].mean()
   married_count= int(filtered_df[filtered_df["marital"]=="married"]['marital'].count() *np.random.choice((1,5)))
   avg_balance=filtered_df["balance_new"].mean()

   with placeholder.container():
       kpi1,kpi2,kpi3=st.columns(3)
       kpi1.metric(label="Age  :scales:",value=round(avg_age),delta=round(avg_age)-10)
       kpi2.metric(label="Married Count  :ring:",value=int(married_count),delta=int(married_count)-10)
       kpi3.metric(label="A/C Balance  :dollar:",value=round(avg_balance),delta=int(avg_balance)+10)

       fig1_col,fig2_col=st.columns(2)

       with fig1_col:
           st.subheader("Chart 1")
           fig=px.density_heatmap(data_frame=filtered_df,y="age_new",x="marital")
           st.write(fig)

       with fig2_col:
           st.subheader("Chart 2")
           fig=px.histogram(filtered_df,x="age_new")
           st.write(fig)
           
       st.subheader("Detail Data View")
       st.write(filtered_df)
       time.sleep(1)

    

