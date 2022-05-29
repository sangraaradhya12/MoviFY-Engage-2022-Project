<br/>

## Submission for Microsoft Engage 2022: Algorithms 

![image001](https://user-images.githubusercontent.com/79754424/167501435-3fea72dd-0e81-4bc3-bb7a-1ca85a715d49.jpg)
<br/>


# `MoviFY` -  The Movie Recommendation System Engine 

### Overview:
**MoviFY:** An online movie recommender web app based on the concept of **Cosine Similarity** , **Matrix Vectorization Method** and **Sorting ALGO**. It first calculate all the similarity scores of the Movies from the Datasets and API{tMDB] and then recommends movies to the user in app.
Where similarity score is a numerical value ranges between zero to one which helps to determine how much two items are like each other on a scale of zero to one. This similarity score is obtained by measuring the similarity between the movie_features of both items. So, the similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
All the details of the movies (title, genre, runtime, rating, images, etc) are fetched using an API by TMDB as well as from the TMDB datasets.

## Important Links:
GitHub Repository URL: https://github.com/sangraaradhya12/MoviFY-Engage-2022-Project <br/>
Presentation Report  :    <br/>

## Functions & Features:

1. Added Administrator authentication which makes the web app secured.

    CREDENTIALS FOR AUTHENTICATON :
```
username : admin
password : 123
```
 2. It consists of mainly 2 Recommendations Algorithm in which there is Sorting-Ranking Algo and Content-Based Filtering method { Vectorization & Cosine_Similarity }. 

 3. Sorts the Movie Data on the basis of either Rating or Popularity and both as well , mainly using the TMBD datassets for the work.

 4. By clicking on the movie frame , the user can get to the ImDB site where Trailers, Directors and Cast Memebers ,etc can be seen . Thus, acting as a resource to know more about the Movie.

 5. User-Interface and UX of the web app can be changed easily by accesing the **.streamlit file** in the repository in there , one can change the background-colors, text-font, primary-color etc. just by varying the data in **config.toml** file.

 6. Cross Platform & Responsive - The site works and looks pretty and have a easy to use , understand and smooth workflow patterns.
 
 7. Gives good recommendations on Datasets used and provides all the information regarding the movies.
 
 8. Rating Level is there to rate the movie(s), one had watched. 
 
 9. Search for Movies based on different keywords(Titles,Genres,Actors,Directors etc.)
 
 10. One can also add movie to the watchlist section.
 
 ## Technologies / Libraries Used :
 ### Main Language : <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
 
 ### Client : Streamlit
 ### Backend-Server : Numpy , Pandas , Scikit-learn
 ### Files : Jupyter-Notebooks
 
 #### Dataset Provider: <img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"/> 
 
 #### Version control: <img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/>
 
 #### IDE:  <img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>      <img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/> 
 
 #### API: TMDB
 

## Installation/Environment Setup:
#### 1. Clone App
 ``` 
  * Clone or download this repository to your local machine.
 ``` 
#### 2. Setting up the files
 * Check whether all the files including(Jupyter-Notebooks) are installed correctly and are there in the data file .

#### 3. Install Requirements.txt
* Install all the libraries mentioned in the [requirements.txt]
```
pip install -r requirements.txt
```

#### 4. Open terminal & Run Commands
* Open your terminal/command prompt from the project directory and run the file `main.py` by executing the following command

```
streamlit run vers1.py
```

#### 5. Open the browser & search the URL
* Now its done, just Go to your browser and type the following URL in the address bar and you are good to go.

``` 
   http:// localhost:8501
```
