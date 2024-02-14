import streamlit as st
import pandas as pd
import pickle 

st.title ("WBSFlix - Movie Recommendations")

st.markdown ( "## find the movies you like with our WBSFlix recommendations!")

st.write("We have tons of popular movies from 1995 to 2018. Yes, we are absolutely old school regarding our movie taste and not up to date.")

st.divider()

st.markdown(" ### the 5 most popular movies of all times:")
popular_movies = pickle.load(open('best_movies.sav', "rb"))

popular_movies_lst = (popular_movies.drop(["movieId","num_ratings","avg_rate"], axis = 1)
                                    .reset_index(drop=True)
                     )
popular_movies_lst
st.divider()
