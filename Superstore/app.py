import os
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='Superstore',page_icon=":bar_chart:",layout="wide")
st.title("  :bar_chart:   Superstore")
st.markdown("<style>div.block-container{padding:1rem};</style>",unsafe_allow_html=True)

file = st.file_uploader(":file_folder: Upload a file",type=['csv','xlsx','txt','xls'])


if file is not None :
    if(file.type=='csv'):
       df= pd.read_csv(file)
    elif (file.type=='.xlsx' or file.type=='application/vnd.ms-excel'):
       df=pd.read_excel(file,sheet_name='Orders')
else :
    df=pd.read_excel("/Users/divyanshuchaturvedi/Documents/Documents/Data Science Practice/Superstore/Superstore datastet.xls",sheet_name='Orders')
    df=pd.read_excel(file,sheet_name='Orders')

#st.write(df)

col1,col2=st.columns(2)

#order date
df['Order Date']=pd.to_datetime(df['Order Date'])
startDate=df['Order Date'].min()
endDate=df['Order Date'].max()

with col1:
    date1=pd.to_datetime(st.date_input("Enter Start Date",startDate))
with col2:
    date2=pd.to_datetime(st.date_input("Enter End Date",endDate))

df_date=df[(df["Order Date"]>=date1) & (df["Order Date"]<=date2)].copy()

#region
st.sidebar.header("Select Your Filter:")
region=st.sidebar.multiselect("Region",df_date["Region"].unique())

if not region:
  df_date_region=df_date.copy()
else :
  df_date_region=df_date[df_date["Region"].isin(region)].copy()

#state
state=st.sidebar.multiselect("State",df_date_region["State"].unique())
if not state :
   df_date_region_state=df_date_region.copy()
else:
   df_date_region_state=df_date_region[df_date_region["State"].isin(state)].copy()

#city
city=st.sidebar.multiselect("City",df_date_region_state["City"].unique())
if not city :
   filtered_df=df_date_region_state.copy()
else:
   filtered_df=df_date_region_state[df_date_region_state["City"].isin(city)].copy()

st.write(filtered_df)



