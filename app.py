import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c5bdd5b9796c2057a0e604f3e3a902cf&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

movies_dic=pickle.load(open('movies_dict.pkl','rb'))
moviess = pd.DataFrame(movies_dic)

similarities=pickle.load(open('similarities.pkl','rb'))

def recommend(movies):
    movie_index=moviess[moviess['title']==movies].index[0]
    distance=similarities[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=moviess.iloc[i[0]].id
        recommended_movies.append(moviess.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_posters(movie_id))
    return recommended_movies,recommended_movies_posters

st.title('Movie recommendation system')
selected_movie_name= st.selectbox(
    'How would you like to be contacted',
    moviess['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])