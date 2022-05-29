# MoviFY-Engage-2022-Project / Microsoft Engage 2022: Algorithms 
## MoviFY - A Movie Recommendation System Engine 

### Overview:
**MoviFY:** An online movie recommender web app based on the concept of **Cosine Similarity** , **Matrix Vectorization Method** and **Sorting ALGO**. It first calculate all the similarity scores of the Movies from the Datasets and API{tMDB] and then recommends movies to the user in app.
Where similarity score is a numerical value ranges between zero to one which helps to determine how much two items are like each other on a scale of zero to one. This similarity score is obtained by measuring the similarity between the movie_features of both items. So, the similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
All the details of the movies (title, genre, runtime, rating, images, etc) are fetched using an API by TMDB as well as from the TMDB datasets.

## Important Links:
GitHub Repository URL: https://github.com/kshitiz-patel/Microsoft-Engage-Algorithms <br/>
Video Demo: https://youtu.be/DvFyBJbeyoE<br/>

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
 8. 

## Installation/Environment Setup:
#### 1. Clone App
  
  * Clone or download this repository to your local machine.
  
#### 2. Setting up the files


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
   http:// localhost:
```
