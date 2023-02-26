![TS](https://user-images.githubusercontent.com/121713702/220956201-c4f38d16-cf71-4ef8-8e5b-109edc1af9c8.png)


# What is Twitter Scraping?
  Scraping is a technique to get information from Social Network sites. Scraping Twitter can yield many insights into sentiments, opinions and social media trends. Analysing tweets, shares, likes, URLs and interests is a powerful way to derive insight into public conversations.
  It is legal to scrape Twitter or any other SNS(Social Networking Sites) to extract publicly available information, but you should be aware that the data extracted might contain personal data.
  
# How to Scrape the Twitter Data?
  Scraping can be done with the help of many opensource libraries like 
	
  1. Tweepy
  2. Twint
  3. Snscrape
  4. Getoldtweets3
  
  For my project I have used SNSCRAPE library.
   
# Libraries and Modules needed for the project!

 1. snscrape.modules.twitter - (To Scrape the Data from Twitter)
 2. Pandas - (To Create a DataFrame with the scraped data)
 3. Pymongo - (To upload the dataframe to MongoDB database)
 4. Streamlit - (To Create Graphical user Interface)
 5. Datetime - (To get the current date)
	

# Snscrape
  Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on. Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others. Its advantages are that there are no limits to the number of tweets you can retrieve or the window of tweets (that is, the date range of tweets). So Snscrape allows you to retrieve old data.

# Streamlit
  Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. Streamlit allows you to re-use any Python code you have already written. This can save considerable amounts of time compared to non-Python based tools where all code to create visualizations needs to be re-written.
  
  In my project I've extensively used streamlit API Reference feature for creation of Titles, Images, Headers, Input boxes, Buttons, Checkbox, Download buttons.
 
  To know more about Streamlit do visit the official site- https://docs.streamlit.io/library/api-reference
  
# Workflow
  Lets us see the workflow of the twitter scraping project by breakingdown it step by step.
  
### Step 1
  Importing the libraries.
  As I have already mentioned above the list of libraries/modules needed for the project. First we have to import all those libraries. Before that check if the libraries are already installed or not by using the below piece of code.
  	
	!pip install ["Name of the library"]
	
  If the libraries are already installed then we have to import those into our script by mentioning the below codes.
  	
	import snscrape.modules.twitter as sntwitter
	import pandas as pd
	import pymongo
	import streamlit as st
	from datetime import date	
### Step 2
  Getting inputs from the user. In the below code I have created the list of variables for getting user input.
  
  1. Keyword or Hashtag the user needed to search for **(hashtag)**
  2. Number of tweets the user wants to scrape **(tweets_count)**
  3. Tweets posted since date **(start_date)**
  4. Tweets posted until date **(end_date)**
  5. Date when the user is scraping the tweets **(today)**. Im getting this date with the help of **datetime** module 
  
	hashtag = st.sidebar.text_input("Enter the keyword or Hashtag you need to get : ")
	tweets_count = st.sidebar.number_input("Enter the number of Tweets to Scrape : ", min_value= 1, max_value= 1000, step= 1)
	start_date = st.sidebar.date_input("Start date (YYYY-MM-DD) : ")
	end_date = st.sidebar.date_input("End date (YYYY-MM-DD) : ")
	today = str(date.today())

  

  

  
  
  
  
  
  
  
