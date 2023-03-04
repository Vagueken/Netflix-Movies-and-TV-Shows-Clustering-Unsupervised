import streamlit as st 
import pickle
import pandas as pd


def recommend_10(movie): 
    movie_index = movies[movies['title'] == movie].index[0] ##fetching the movie index
    distances = cosine_similarity[movie_index]
    top10 = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:11]
    # list with the titles of the best 10 matching movies
    recommended_movies = []
    for i in top10:
      recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
  
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

cosine_similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2013/07/13/01/10/homer-simpsons-155238_1280.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

option = st.selectbox('Select your Movie:', movies['title'].values)


if st.button('Recommend'):
  recommendations = recommend_10(option)
  for i in recommendations:
    st.write(i)








