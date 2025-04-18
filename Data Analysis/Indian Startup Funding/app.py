import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import Database


db=Database()

df=db.df

def overall_analysis():
    st.title("Overall")
    total,max_investment,avg_investment,startup_count,year_month_df=db.overall_analysis()
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Total',str(round(total))+" Crs")
    with col2:
        st.metric('Max Investment',str(round(max_investment))+ ' Crs')
    with col3:
        st.metric('Average Investment',str(round(avg_investment))+' Crs')
    with col4:
         st.metric('Total Startups',startup_count)

        
    st.subheader("MoM Analysis")

    option_selected=st.selectbox("Choose the type",options=['Number of Startups','Amount Invested'])
    if option_selected=='Number of Startups':
        fig,ax=plt.subplots()
        ax.plot(year_month_df['year_month'],year_month_df['startupname'])
        st.pyplot(fig)
    else:
        fig,ax=plt.subplots()
        ax.plot(year_month_df['year_month'],year_month_df['amount'])
        st.pyplot(fig)


def investor_analysis(investor_selection):
        st.title(investor_selection)
        recent_investment,bigggest_investment,sector_investments,round_investments,city_investments,year_investments=db.investor_analysis(investor_selection)
        st.subheader("Recent Investment")
        st.write(recent_investment)
       
        col1,col2=st.columns(2)
        with col1:
            st.subheader("Biggest Investment")
            fig,ax=plt.subplots()
            ax.bar(bigggest_investment.index,bigggest_investment.values)
            st.pyplot(fig)
        with col2:
            st.subheader("Sector Wise Investment")
            fig1,ax1=plt.subplots()
            ax1.pie(sector_investments,labels=sector_investments.index,autopct='%0.01f%%')
            st.pyplot(fig1)

        col1,col2=st.columns(2)
        with col1:
            st.subheader("Round Investment")
            fig,ax=plt.subplots()
            ax.pie(round_investments,labels=round_investments.index,autopct='%0.01f%%')
            st.pyplot(fig)
        with col2:
            st.subheader("City Wise Investment")
            fig,ax=plt.subplots()
            ax.pie(city_investments,labels=city_investments.index,autopct='%0.01f%%')
            st.pyplot(fig)

        st.subheader("Year Wise Investment")
        fig,ax=plt.subplots()
        ax.plot(year_investments.index,year_investments.values)
        st.pyplot(fig)
        


st.set_page_config(layout='wide',page_title='Startup Analysis')
st.sidebar.title("Indian Startups")

user_selection=st.sidebar.selectbox("Select Analysis",["Overall","Startup","Investors"])

if user_selection=="Overall":
       overall_analysis()
   

if user_selection=="Startup":
    st.title("Startup")
    startup_selection=st.sidebar.selectbox("Select Startup",sorted(df['startupname'].unique()))
    startup_btn=st.sidebar.button("Find Startup Details")

elif user_selection=="Investors":
    #st.title("Investors")
    investor_selection=st.sidebar.selectbox("Select Investor",sorted(set(df['investor'].str.split(',').sum())))
    startup_btn=st.sidebar.button("Find Investor Details")
    if startup_btn:
         investor_analysis(investor_selection)
        
