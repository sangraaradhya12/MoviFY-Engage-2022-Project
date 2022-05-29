from requests import request
import requests
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from content_based_ui import content_based_ui
from basic_ui import basic_recommender_ui
from collaborative_ui import collaborative_ui
from streamlit_lottie import st_lottie
from watchlist import watchlist


st.set_page_config(
    layout="wide", page_title="MoviFY", page_icon="Images/logo1.png"
)

###### CUSTOM CSS STYLING #######
style = f"""
<style>
.appview-container .main .block-container{{
        padding-top: 2em;    }}
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
    transform: scale(1.1);
}}
</style>"""
st.markdown(style, unsafe_allow_html=True)

### LOGIN PAGE MADE AS ADMINISTRATOR #######

names = ['Administrator']
usernames = ['admin']
passwords = ['123']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

    ######## LOTTIE ANIMATIONS TOP ##############


def load_lottieur(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_project = load_lottieur(
    "https://assets6.lottiefiles.com/packages/lf20_cbrbre30.json")

st_lottie(lottie_project, height="100px", key=None)

########## LIST OF RECOMMENATION ALGORITHMS ##########################
recommenders = [
    "Sorting on Ratings/Reviews",
    "Users Filtering",
    "Filtering by Content-Based",

]
##############################################################################################

####### INITIALIZING DATASETS #############
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

    ####### MAKING THE COMMON UI WORK ########
if len(st.session_state["watchlist"].movies_list) > 0:
    with st.sidebar.expander("My Watchlist"):
        st.write(
            pd.Series(st.session_state["watchlist"].movies_list, name="Title"))

st.title(" See What's Next in the Movie(s) !!! ")
st.sidebar.title(" Search using Different Recommendation Algo's  ")
recommender_type = st.sidebar.selectbox(" Types : ", recommenders)
#################################################################################################

############## SIMPLE RECOMMENDATIONS UI {GENRE} ###############
if recommender_type == recommenders[0]:

    ### INITIALISE A BASIC RECOMMENDER UI RENDERING OBJECT ################
    if "basic_recommender_ui" not in st.session_state:
        st.session_state["basic_recommender_ui"] = basic_recommender_ui(
            st.session_state["datasets"]["links"]
        )
    #######################################################################

    st.session_state["basic_recommender_ui"].render()
##################################################################################################

    ############## CONTENT BASED FILTERING UI #################
elif recommender_type == recommenders[2]:

    #### INITIALISE RENDERING OBECT ############
    if "content_based_ui" not in st.session_state:
        st.session_state["content_based_ui"] = content_based_ui(
            st.session_state["datasets"]["links"]
        )

    st.session_state["content_based_ui"].render()

###################################################################################################

    ####### USERS FILTERING COLLAB UI ##############
elif recommender_type == recommenders[1]:

    if "collaborative_ui" not in st.session_state:
        st.session_state["collaborative_ui"] = collaborative_ui(
            st.session_state["datasets"]["links"]
        )
    #######################################################################

    st.session_state["collaborative_ui"].render()
#####################################################################################################
