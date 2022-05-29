
import streamlit as st
import pandas as pd
import numpy as np
from content_based_filtering import content_based_filter
from images_picture import images_picture


class content_based_ui:

    ######## GET INITIALISE REQUIRED DATA AND OBJECTS' #################
    def __init__(self, links):
        self.recommender = content_based_filter(links)
        self.movies_list = self.recommender.get_movies_list()
        self.features_list = [
            "title",

            "genres",
            "keywords",
            "actors",
            "directors",
            "ranks"
        ]
        self.choices = [
            "Recommend similar Movies based on watching",
            "By Using the Keywords to search specific data",
        ]
        self.images_picture = images_picture()

    ##################################################################

    ##### CACHE DIFFERENT COMBINATIONS FEATURES WHILE SORTING #############
    @st.cache
    def update_features_list(features_to_include):
        self.recommender.update_features_combination(features_to_include)

    ##############################################################################

    def render(self):

        #### CHOOSE WHETHER TO INPUT A MOVIE OR KEYWORD'S #####
        content_choice = st.sidebar.radio(
            "Get the movies based on these options :",
            self.choices,
        )
        ####################################################

        st.sidebar.write(" ")

        ## SELECT COLUMNS/FEATURES TO MATCHING ####################
        with st.sidebar.expander(
            "Keywords include"
            if content_choice == self.choices[1]
            else "Match movies by:"
        ):
            features_columns = st.columns(2)
            title = features_columns[0].checkbox("Title", value=True)
        # synopsis = features_columns[1].checkbox("Synopsis", value=True)
            genres = features_columns[0].checkbox("Genres", value=True)
            actors = features_columns[1].checkbox("Actors", value=True)
            keywords = features_columns[0].checkbox("Tags", value=True)
            directors = features_columns[1].checkbox("Directors", value=True)
        ######################################################################################

        features_to_include = {

            "title": title,
            # "synopsis": synopsis,
            "genres": genres,
            "keywords": keywords,
            "actors": actors,
            "directors": directors,
        }

        ###### INPUT USER'S FAV MOVIES OR KEYWORDS ##############
        if content_choice == self.choices[1]:
            custom_movie_summary = st.text_input("Enter keywords to search :")
        else:
            custom_movie_titles = st.multiselect(
                " Get the Movies to search for :",
                self.movies_list,
            )
            custom_movie_summary = self.recommender.get_features(
                custom_movie_titles)
        ##############################################################################

        ##### GENERATE MOVIE RECOMMENDATIONS ##############################################
        content_recommendations = self.recommender.recommend(
            features_to_include,
            custom_movie_summary,
        )
        #############################################################################

        self.images_picture.print(rec=content_recommendations)
