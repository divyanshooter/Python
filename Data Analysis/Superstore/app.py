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


if file:
    if(file.type=='csv'):
       df= pd.read_csv(file)
    elif (file.type=='.xlsx' or file.type=='application/vnd.ms-excel'):
       df=pd.read_excel(file,sheet_name='Orders')
else :
    df=pd.read_excel("/Users/divyanshuchaturvedi/Documents/Documents/Data Science Practice/Superstore/Superstore datastet.xls",sheet_name='Orders')
    #df=pd.read_excel(file,sheet_name='Orders')

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

# st.write(filtered_df)

category_df=filtered_df.groupby(by="Category",as_index=False)["Sales"].sum()

with col1:
   st.subheader("Category wise Sales")
   fig=px.bar(category_df,x="Category",y="Sales",text=['${:,.2f}'.format(x) for x in category_df["Sales"]],template="seaborn")
   st.plotly_chart(fig,use_container_width=True,height=200)

with col2:
   st.subheader("Region wise Sales")
   fig=px.pie(filtered_df,names="Region",values="Sales",hole=0.5)
   fig.update_traces(text=filtered_df["Region"],textposition="outside")
   st.plotly_chart(fig,use_container_width=True,height=200)

cl1,cl2=st.columns(2)

with cl1:
   with st.expander("Category_Wise Data"):
      st.write(category_df.style.background_gradient(cmap="Blues"))
      csv=category_df.to_csv(index=False).encode("utf-8")
      st.download_button("Download Data",data=csv,file_name="Category.csv",mime="text/csv"
                         ,help="Click here to download data as csv")
with cl2:
   with st.expander("Region_Wise Data"):
      region_df=filtered_df.groupby("Region",as_index=False)["Sales"].sum()
      st.write(region_df.style.background_gradient(cmap="Oranges"))
      csv=region_df.to_csv(index=False).encode("utf-8")
      st.download_button("Download Data",data=csv,file_name="Region.csv",mime="text/csv"
                         ,help="Click here to download data as csv")

filtered_df["month_year"]=filtered_df["Order Date"].dt.to_period("M")

st.subheader("Time Series Analysis")

linechart=pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart,x="month_year",y="Sales",labels={"Sales":"amount"},template="gridon",height=500,width=1000)
st.plotly_chart(fig2,use_container_width=True)

with st.expander("View Data of Time Series"):
   st.write(linechart.T.style.background_gradient(cmap="Blues"))
   csv=linechart.to_csv(index=False).encode("utf-8")
   st.download_button("Download Data",data=csv,file_name="Time Series.csv",mime="text/csv"
                         ,help="Click here to download data as csv")

st.subheader("Heirarhical Data")
fig3=px.treemap(filtered_df,path=["Region","Category","Sub-Category"],values="Sales",
                hover_data=["Sales"],color="Sub-Category")
st.plotly_chart(fig3,use_container_width=True)

chart1,chart2 = st.columns((2))

with chart1:
   st.subheader("Segment Wise Sales")
   fig=px.pie(filtered_df,values="Sales",names="Segment",template="plotly_dark")
   fig.update_traces(text=filtered_df["Segment"],textposition="inside")
   st.plotly_chart(fig,use_container_width=True)

with chart2:
   st.subheader("Category Wise Sales")
   fig=px.pie(filtered_df,values="Sales",names="Category",template="gridon")
   fig.update_traces(text=filtered_df["Category"],textposition="inside")
   st.plotly_chart(fig,use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Month Wise Sub-Category Sales Summary")
with st.expander("Summary_Table"):
   df_sample=df[0:5][["Region","State","City","Category","Sales","Profit","Quantity"]]
   fig=ff.create_table(df_sample,colorscale="Cividis")
   st.plotly_chart(fig)

   st.markdown("Month Wise sub-Category Table")
   filtered_df["Month"]=filtered_df["Order Date"].dt.month_name()
   sub_category_Year= pd.pivot_table(data=filtered_df,values="Sales",index=["Sub-Category"],columns="Month")
   st.write(sub_category_Year.style.background_gradient(cmap="Blues"))

data1= px.scatter(filtered_df,x="Sales",y="Profit",size="Quantity")
data1['layout'].update(title="Relationship between Sales and Quantity usning Scatter PLot."
                       ,titlefont=dict(size=20),xaxis=dict(title="Sales",titlefont=dict(size=19)),
                       yaxis=dict(title="Profit",titlefont=dict(size=19)))
st.plotly_chart(data1,use_container_width=True)

with st.expander("View Data"):
   st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

csv=df.to_csv(index=False).encode("utf-8")
st.download_button("Download Data",data=csv,file_name="Data.csv",mime="text/csv")

