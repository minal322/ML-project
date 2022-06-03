# can use flask also but for this project i am using streamlit

import streamlit as st
import pickle
import pandas as pd
import requests
import base64
st.set_page_config(layout="wide")
def fetchposter(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    print()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x:x[1])[1:8]

    recommended_movies = []
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id_x
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetchposter(movie_id))
    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select Any movie and click Recommend ',
    (movies['title'].values)
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
    with col1:
        st.text(names[0])
        st.image(posters[0],use_column_width=True,width=500)
    with col2:
        st.text(names[1])
        st.image(posters[1],use_column_width=True, width=500)
    with col3:
        st.text(names[2])
        st.image(posters[2],use_column_width=True, width=500)
    with col4:
        st.text(names[3])
        st.image(posters[3],use_column_width=True, width=500)
    with col5:
        st.text(names[4])
        st.image(posters[4],use_column_width=True, width=500)
    with col6:
        st.text(names[5])
        st.image(posters[5],use_column_width=True, width=500)
    with col7:
        st.text(names[6])
        st.image(posters[6],use_column_width=True, width=500)



