import streamlit as st
import pandas as pd
from content_based_ui import content_based_ui
from basic_ui import basic_recommender_ui
from collaborative_ui import collaborative_ui
from watchlist import watchlist

st.set_page_config(
    layout="wide", page_title="MoviFY", page_icon="Images/logo.jpg"
)

#### CUSTOM CSS STYLING #####################################################################
style = f"""
<style>
.appview-container .main .block-container{{
        padding-top: 2rem;    }}
footer, header{{
    visibility: hidden;
}}
.movie-poster + div > .stButton, .movie-poster + div>.stButton>button{{
    font-size: 20px;
    width:100% !important;
    border-top:none;
    border-left: none;
    border-right:none;
    border-radius: 0px;
    background-color: white;
}}
.stButton, .stButton>button{{
    width: 100% !important;
}}
.movie-poster{{
    tranform: translateZ(10px);
}}
.movie-poster:hover{{
    transform: scale(1.2);
}}
</style>"""
st.markdown(style, unsafe_allow_html=True)
##############################################################################################

##################### LIST OF RECOMMENATION ALGORITHMS #######################################
recommenders = [
    "Sorting by Ratings",
    "Content-Based Search",
    "Collab- Based Searching(user) ",
]
##############################################################################################

# INITIALIZING DATASETS ######################################################################
if "datasets" not in st.session_state:
    st.session_state["datasets"] = {
        "links": pd.read_csv(
            "Datasets/links.csv",
            index_col=[0],
            dtype={"movieId": int, "imdbId": str,
                   "tmdbId": str, "imdb_link": str},
        ),
    }
if "watchlist" not in st.session_state:
    st.session_state["watchlist"] = watchlist()
################################################################################################

####### SETTING UP THE COMMON UI ELEMENTS ######################################################
if len(st.session_state["watchlist"].movies_list) > 0:
    with st.sidebar.expander("My Watchlist"):
        st.write(
            pd.Series(st.session_state["watchlist"].movies_list, name="Title"))
st.title(" See What's Next in the Movie(s) !!! ")
st.sidebar.title(" Search using Different Recommendation Algo's  ")
recommender_type = st.sidebar.selectbox(" Types : ", recommenders)
#################################################################################################

############## UI FOR BASIC RECOMMENDER (Genre Based) ###########################################
if recommender_type == recommenders[0]:

    ### INITIALISE A BASIC RECOMMENDER UI RENDERING OBJECT ################
    if "basic_recommender_ui" not in st.session_state:
        st.session_state["basic_recommender_ui"] = basic_recommender_ui(
            st.session_state["datasets"]["links"]
        )
    #######################################################################

    st.session_state["basic_recommender_ui"].render()
##################################################################################################


############## UI FOR CONTENT BASED FILTERING ####################################################
elif recommender_type == recommenders[1]:

    #### INITIALISE A CONTENT-BASED UI RENDERING OBECT ############
    if "content_based_ui" not in st.session_state:
        st.session_state["content_based_ui"] = content_based_ui(
            st.session_state["datasets"]["links"]
        )
    ###############################################################
    st.session_state["content_based_ui"].render()

###################################################################################################


##### UI for Collaborative Filtering ##############################################################
elif recommender_type == recommenders[2]:

    ### INITIALISE A COLLABORATIVE FILTERING UI RENDERING OBJECT ##########
    if "collaborative_ui" not in st.session_state:
        st.session_state["collaborative_ui"] = collaborative_ui(
            st.session_state["datasets"]["links"]
        )
    #######################################################################

    st.session_state["collaborative_ui"].render()
#####################################################################################################
