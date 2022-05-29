import streamlit as st
import pandas as pd
import numpy as np
from simple_recommendations import basic_recommender
from images_picture import images_picture


class basic_recommender_ui:

    ########### INITIALISE REQUIRED DATA AND OBJECTS ########
    def __init__(self, links_data):
        self.images_picture = images_picture()
        self.recommender = basic_recommender(links_data)
        self.genres_list = self.recommender.get_genres()

    #########################################################

    #### CACHE DIFFERENT COMBINATIONS OF RATING AND POPULARITY WEIGHTAGE WHILE SORTING ####
    @st.cache(allow_output_mutation=True)
    def sort_movies(self, weightages):
        return self.recommender.recommend(weightages[0], weightages[1])

    #######################################################################################

    #### FINAL RECOMMENDATION FUNCTION TO SORT AND THEN FILTER GENRES #######################
    def genre_based_rec(self, genres, weightages):
        recommendations = self.sort_movies(
            weightages
        )  # DO NOT CHANGE recommendations IN THIS FUNCTION (TO AVOID MODIFYING CACHE)
        if len(genres) == 0:
            return recommendations.head(50)
        genre_count = recommendations.apply(
            lambda x: len(set(x["genres"].split(" ")).intersection(genres)),
            axis=1,
        )
        return recommendations[[i > 0 for i in genre_count]].head(50)

    #########################################################################################

    def render(self):
        selected_genres = st.sidebar.multiselect(
            "Select your favourite genres", self.genres_list)
        st.write(
            """
            ### Stream the Best Movies Here :)
        """
        )
        st.sidebar.write(" ")
        with st.sidebar.expander("Sort By :"):
            weightage_columns = st.columns(2)
            rating_weightage = int(
                weightage_columns[0].checkbox("Rating", value=True))
            votes_weightage = int(weightage_columns[1].checkbox("Popularity"))

        genre_recommendations = self.genre_based_rec(
            selected_genres, [rating_weightage, votes_weightage]
        )

        st.sidebar.write(" ")
        with st.sidebar.expander("Search All"):
            weightage_columns = st.columns(3)
            rating_weightage = int(
                weightage_columns[1].checkbox("Movie Reviews", value=True))

        st.sidebar.subheader("Created by Aradhya Sangra")
        self.images_picture.print(rec=genre_recommendations)
