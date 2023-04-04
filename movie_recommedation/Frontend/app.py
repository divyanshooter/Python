import streamlit as st
import pandas as pd
import pickle

movies_dict=pickle.load(open("movies.pkl","rb"))
movies=pd.DataFrame(movies_dict)

similarity= pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations=[]
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'Please select your movie',
    movies['title'].values)

if st.button('Recommend'):
    recommended_movies =recommend(selected_movie)
    for i in recommended_movies:
        st.write(i)
