# predictiing-billboad-hits-using-spotify-data-deploy

# Billboard-Hit-Predictor
# PROJECT REPORT


# TITLE: Hit Predict-Predicting Billboard Hits Using Spotify Data
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 001](https://user-images.githubusercontent.com/57080465/130446162-c75c34d2-9066-45da-8059-b3382d04b4dc.jpeg)

# AIM:
  The principle focus of our project is to perform data analysis and train a model using the most popular Machine Learning algorithms like Logistics Regression, Linear and Quadratic Discriminant Analysis Support Vector Machine, Random Forest Classifier, etc in order to analyze the historical data that is present in different data sources like Spotify data, Million Songs Data and Billboard Charts data put all together.

# ABSTRACT:
  The Billboard Hot 100 Chart1 remains one of the definitive ways to measure the success of a popular song. We investigated using machine learning techniques to predict which songs will become Billboard Hot 100 Hits. 

# INTRODUCTION:
  •	We extracted different audio features from the Spotify API4 (Table 1).
  
  ![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 002](https://user-images.githubusercontent.com/57080465/130446468-0053120b-d189-4145-b430-aa69910d7c4a.png)
  
  •	We created the Artist Score metric, assigning a score of 1 to a song if the artist previously had a Billboard hit, and 0 otherwise.
  
  ![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 003](https://user-images.githubusercontent.com/57080465/130446555-4f8b19f3-3cd4-408c-b4de-be2a523b76f0.png)
  
  •	Data for ~4000 songs was collected from Billboard.com3 and the Million Song Dataset5. Songs were from 1990-2018. 
  
  •	Songs were labeled 1 or 0 based on Billboard success. 
  
  •	Audio features for each song were extracted from the Spotify Web API4. 
  
  •	Different machine-learning algorithms were used to predict a song’s Billboard success.

# OVERVIEW:
  •	Data Segmentation and Data Cleaning
  
  •	Exploratory Data Analysis using python’s data visualization libraries.
  
  •	Training the model based on the historical data available.

# DATASET:
  
  ![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 004](https://user-images.githubusercontent.com/57080465/130446805-98d9c497-fe70-4749-a380-6b8be7a9ac38.png)
  
  •	SpotifyID: Unique ID for tracks in Spotify API.
  
  •	Track: Track Name.
  
  •	Artist: Track performer/singer/band.
  
  •	Danceability: Danceability is measured using a mixture of song features such as beat strength, tempo stability, and overall tempo.
  
  •	Energy: song energy is the sense of forward motion in music, whatever keeps the listener engaged and listening.
  
  •	Key:  the key of a piece is the group of pitches, or scale, that forms the basis of a song.
  
  •	Mode: mode, in music, any of several ways of ordering the notes of a scale according to the intervals they form with the tonic, thus providing a theoretical framework for the melody.
  
  •	Speechiness: Speechiness detects the presence of spoken words in a track. 
  
  •	Instrumentalness: This value represents the amount of vocals in the song.
  
  •	Liveness: This value describes the probability that the song was recorded with a live audience.
  
  •	Valence:  Describes the musical positiveness conveyed by a track. 
  
  •	Tempo:  tempo is how fast or slow a piece of music is performed.
  
  •	Duration_ms: Track duration in millisecond.
  
  •	Loudness: loudness is the subjective perception of sound pressure.
  
  •	billboard_hit: identifier if the song/track is Hit or Not. (Target)

# DATA SEGMENTATION AND DATA CLEANING:
  •	The dataset had few missing values. We dropped those rows.
  
  •	We treated the outliers with z-score.
  
  •	We checked the distribution of data after outlier treatment 
  
  •	We tried different plots and combination plots, to check the relationship of different features within themselves and with target variables. (Scatter plot, bar plot, distribution plot, correlation heatmap)
  
  •	We performed Hypothesis test with 95% confidence interval, VIF analysis to make sure which features are statistically significant.

# EXPLORATORY DATA ANALYSIS:
# Checking Target Variable is imbalanced or not.
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 005](https://user-images.githubusercontent.com/57080465/130448053-3b42a296-f6e0-4288-a2c7-dad31390ea98.png)
  
  Target variable is not imbalanced.

# Top 10 Energetic Songs
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 006](https://user-images.githubusercontent.com/57080465/130448160-d4dfc817-29fe-41e7-b5b3-d2a0b6702c29.png)

# Top 10 Danceable songs
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 007](https://user-images.githubusercontent.com/57080465/130448243-1dcc567d-2c3a-400e-8cd1-e383e2741b93.png)

# Count of Track Based on Keys
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 008](https://user-images.githubusercontent.com/57080465/130448332-bff81608-62d7-488a-87fb-01ecfa6b6204.png)

# Distribution of song duration 
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 009](https://user-images.githubusercontent.com/57080465/130451546-f582411a-5998-4b98-93e5-ab9308c1a950.png)

# Distribution of track tempo
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 010](https://user-images.githubusercontent.com/57080465/130451629-54850ecc-bd1f-4b12-b897-23f13fc5a3ad.png)

# Relationship Plots: 3D Scatter Plots
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 011](https://user-images.githubusercontent.com/57080465/130451717-443c828c-6d91-47c4-9caf-30dc06009df3.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 012](https://user-images.githubusercontent.com/57080465/130451793-cdd9570c-c580-4c32-a282-bc36c566bade.png)

# Relationship Plots: 2D Scatter Plots
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 013](https://user-images.githubusercontent.com/57080465/130451873-297a076c-df85-4524-a9ee-3fc5fad58e01.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 014](https://user-images.githubusercontent.com/57080465/130451883-0d1c316e-1539-4e8a-9971-2bc3fd7d206c.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 015](https://user-images.githubusercontent.com/57080465/130451894-45e8cafb-a480-4c67-9716-28022e02f3a3.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 016](https://user-images.githubusercontent.com/57080465/130451916-091cb5da-ee87-4460-ab74-1b0f7c9f2cf4.png)

# Overall Relationship plot: correlation heatmap
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 017](https://user-images.githubusercontent.com/57080465/130452150-31adeeeb-eddc-4a88-b15b-d57f41368fc0.png)

# Statistical Significance of Features based on z-test and chi-square test
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 018](https://user-images.githubusercontent.com/57080465/130452237-1c8081c6-b08b-4c57-babb-06d36079e699.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 019](https://user-images.githubusercontent.com/57080465/130452244-7f4380bd-d21b-40da-8b63-f6ac6cb26362.png)

# VIF Plot: Multicollinearity check
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 020](https://user-images.githubusercontent.com/57080465/130452334-bf8e758b-6b2e-41a9-b16e-8af57e0d713b.png)

# MI SCORES
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 021](https://user-images.githubusercontent.com/57080465/130452438-ae94faf4-8d1a-4738-a4b8-6775a3842eb5.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 022](https://user-images.githubusercontent.com/57080465/130452447-9f057a9e-f28d-4083-a98c-0a7e5b480145.png)

# Conclusion based on EDA:
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 023](https://user-images.githubusercontent.com/57080465/130452540-99012153-39a0-4a8c-b15e-9d006e049e0b.png)

# MODEL BUILDING:
# TEAM A:
# QDA:
The features that were taken for training QDA model were:
  
  •	Instrumentalness
  
  •	Acousticness
  
  •	Loudness
  
  •	Energy
  
  •	Duration
  
  •	Valence
  
  •	Danceability
  
  •	Liveness

The QDA model gave a fairly good accuracy of 79% and the classification report is given below:

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 024](https://user-images.githubusercontent.com/57080465/130452845-70d4975e-ab88-4f9c-b32e-2074db1353a4.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 025](https://user-images.githubusercontent.com/57080465/130452854-a30926ab-0fd4-482e-b7c3-85415bece7cb.jpeg)

# LOGISTIC REGRESSION:
The features that were taken for training Logistic Regression model were:

•	Instrumentalness

•	Acousticness

•	Loudness

•	Energy

•	Duration

•	Valence

•	Danceability

•	Liveness

The Logistic Regression model gave a fairly good accuracy of 76% and the classification report is given below: 

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 026](https://user-images.githubusercontent.com/57080465/130453069-7a9571c4-d24b-4d9d-b550-c067fc1b8d75.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 027](https://user-images.githubusercontent.com/57080465/130453076-83af98fe-1ca7-411d-9a19-dd2bcedd603f.png)

# TEAM B:
# RANDOM FOREST:
For Random Forest model, a small change in the features have been done. As we could see above that the MI score is very less for Key(0.000). So, a small feature engineering is done so that the key and mode is combined and made as a single feature ‘Key_mode_ratio’ which gave a fairly good MI score and many musicians also say there is a relationship between key and mode as well.

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 028](https://user-images.githubusercontent.com/57080465/130453331-6c038e58-e725-4b82-923b-75c0cbcd72a9.png)

The random forest model gave about 81% accuracy which was best among all the models.

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 029](https://user-images.githubusercontent.com/57080465/130453569-09e3ee3c-d355-43d6-b00c-7fb05a8704f6.png)

The confusion matrix of the random forest model is given below:

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 030](https://user-images.githubusercontent.com/57080465/130453876-df063bfd-a15c-4105-9a94-5d48c110f11a.png)

# SVM:
The features that were taken for training Logistic Regression model were:
  
  •	Instrumentalness
  
  •	Acousticness
  
  •	Loudness
  
  •	Energy
  
  •	Duration
  
  •	Valence
  
  •	Danceability
  
  •	Key_mode_ratio
  
  •	Tempo
  
  •	Speechiness
  
  •	Liveness

The SVM model gave about 79-80% accuracy which was also a good accuracy. 

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 031](https://user-images.githubusercontent.com/57080465/130454208-d9cb7b4a-b74a-42ad-9f39-8a36197c3b4c.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 032](https://user-images.githubusercontent.com/57080465/130454215-e8e06121-8a55-4039-98aa-88031bc74ed8.png)

# DEPLOYMENT:
# TEAM A:
# FLASK SERVER DEPLOYMENT:
The logistic regression model is deployed using flask server and Heroku into a real time website.
The link to the website is: https://bhp-flask-heroku.herokuapp.com/

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 033](https://user-images.githubusercontent.com/57080465/130454512-a59cd3a7-699b-446e-b5cd-ddf8f8e6216c.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 034](https://user-images.githubusercontent.com/57080465/130454520-26b1df28-e708-42ab-bb29-3542febcc7cf.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 035](https://user-images.githubusercontent.com/57080465/130454580-a181576f-af4f-445c-b80a-6812afcdc606.png)

# STREAMLIT DEPLOYEMENT:
The QDA model is deployed using streamlit and Heroku into a real time website.
The link to the website is:   https://bhp-streamlit-heroku.herokuapp.com/

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 036](https://user-images.githubusercontent.com/57080465/130454685-f62cd152-4e8d-40e9-b8f9-f53d44f08c26.jpeg)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 037](https://user-images.githubusercontent.com/57080465/130454693-6f1305be-2b9d-43c6-ad00-8c9236ebb2e1.jpeg)

# TEAM B:
# FLASK SERVER DEPLOYMENT:
The random forest model is deployed using flask server and Heroku into a real time website.
The link to the website is: https://billboard-hit-predictor.herokuapp.com/

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 038](https://user-images.githubusercontent.com/57080465/130455095-bf1aa4e0-9863-4966-b7b8-56056438f003.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 039](https://user-images.githubusercontent.com/57080465/130455114-1eae5fcd-95c4-4abc-a0b3-79e9e780abb5.png)

# STREAMLIT DEPLOYEMENT:
The random forest model is deployed using streamlit and Heroku into a real time website.
The link to the website is:   https://billboard-hit-streamlit.herokuapp.com/

![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 040](https://user-images.githubusercontent.com/57080465/130455220-04c2265f-5694-4d23-ac03-1d1999817c33.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 041](https://user-images.githubusercontent.com/57080465/130455229-6e74e473-0748-4dcc-a705-6a81323b68e7.png)
![Aspose Words e3be7d84-9979-45bf-a905-a73badae9465 042](https://user-images.githubusercontent.com/57080465/130455236-ccbda091-4e65-427a-9fa8-268e9a44f2e9.png)


# TEAM MEMBERS:
# TEAM A:
ANJUM HASSAN(TEAM LEADER)

DHAVAL

DEEPAK

ABHISHEK

MANOJ

SHIVA KUMAR

# TEAM B:
VISHAL K B(TEAM LEADER)

NITESH KUMAR G

MARIA

NIHARIKA

SALIK SHAIKH

# MENTORS: 
RANIT SEN 

YASEEN SHAH
