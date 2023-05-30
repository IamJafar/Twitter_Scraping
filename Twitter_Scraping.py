# importing libraries and modules needed for the project
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st
from datetime import date

# twitter scraping image,Titles and sub-heading
st.image("TS.png")
st.subheader("Scrape Tweets with any keywords or Hashtag as you wish!")
st.sidebar.title("**:blue[:wave: Hello there!!!]**")
st.sidebar.header("**:blue[Kindly fill the below details to begin Scraping Tweets] :point_down:**")

# Variable declaration for user inputs(Keyword and Number of tweets)
hashtag = st.sidebar.text_input("Enter the keyword or Hashtag you need to get : ")
tweets_count = st.sidebar.number_input("Enter the number of Tweets to Scrape : ", min_value= 1, max_value= 1000, step= 1)
st.sidebar.subheader(":blue[Select the date range] :calendar:")
start_date = st.sidebar.date_input("Start date (YYYY-MM-DD) : ")
end_date = st.sidebar.date_input("End date (YYYY-MM-DD) : ")
today = str(date.today())

# Creating an empty list
tweets_list = []
# Enabling the Checkbox only when the hashtag is entered
if hashtag:
    st.sidebar.checkbox("**Scrape Tweets**")
    
    # Using for loop, TwitterSearchScraper and enumerate function to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f"{hashtag} since:{start_date} until:{end_date}").get_items()):
        if i >= tweets_count:
            break
        tweets_list.append([tweet.date,
                            tweet.id,
                            tweet.url,
                            tweet.rawContent,
                            tweet.user.username,
                            tweet.replyCount,
                            tweet.retweetCount,
                            tweet.likeCount,
                            tweet.lang,
                            tweet.source
                           ])
else:
    st.sidebar.checkbox("**Scrape Tweets**",disabled=True)
        
# Creating DataFrame with the scraped tweets
def data_frame(data):
    return pd.DataFrame(data, columns= ['datetime', 'user_id', 'url', 'tweet_content', 'user_name',
                                         'reply_count', 'retweet_count', 'like_count', 'language', 'source'])

# Converting DataFrame to CSV file
def convert_to_csv(c):
    return c.to_csv().encode('utf-8')

# Converting DataFrame to JSON file
def convert_to_json(j):
    return j.to_json(orient='index')

# Creating objects for dataframe and file conversion
df = data_frame(tweets_list)
csv = convert_to_csv(df)
json = convert_to_json(df)

# Bridging a connection with MongoDB Atlas and Creating a new database(twitterscraping) and collections(scraped_data)
client = pymongo.MongoClient("your unique client id")
db = client.twitterscraping
col = db.scraped_data
scr_data = {"Scraped_word" : hashtag,
            "Scraped_date" : today,
            "Scraped_data" : df.to_dict('records')
           }

# BUTTON 1 - To view the DataFrame
if st.button("View DataFrame"):
    st.success("**:blue[DataFrame Fetched Successfully]**", icon="✅")
    st.write(df)
    
# BUTTON 2 - To upload the data to mongoDB database
if st.button("Upload the data to MongoDB"):
    try:
        col.delete_many({}) #Deleting old records from the collection
        col.insert_one(scr_data)
        st.success('Upload to MongoDB Successful!', icon="✅")
    except:
        st.error('You cannot upload an empty dataset. Kindly enter the information in the leftside menu.', icon="🚨")

# Header Diff Options to download the dataframe
st.subheader("**:blue[To download the data use the below buttons :arrow_down:]**")

# BUTTON 3 - To download data as CSV
st.download_button(label= "Download data as CSV",
                   data= csv,
                   file_name= 'scraped_tweets_data.csv',
                   mime= 'text/csv'
                  )

# BUTTON 4 - To download data as JSON
st.download_button(label= "Download data as JSON",
                   data= json,
                   file_name= 'scraped_tweets_data.json',
                   mime= 'text/csv'
                  )
