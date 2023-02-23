# importing libraries and modules needed for the project
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
import streamlit as st

# twitter scraping image and sub heading
st.image("TS.png")
st.subheader("Scrape Tweets with any keywords or Hashtag as you wish!")

# Variable declaration for user inputs
hashtag = st.text_input("Enter the keyword or Hashtag you need to get : ")
tweets_count = st.number_input("Enter the number of Tweets to Scrape : ", min_value= 1, max_value= 1000, step= 1)
start_date = st.date_input("Select Start date (YYYY-MM-DD) : ")
end_date = st.date_input("Select End date (YYYY-MM-DD) : ")

# Creating an empty list
tweets_list = []

if hashtag and tweets_count:
    
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
        
# Creating DataFrame with the scraped tweets
def data_frame(data):
    return pd.DataFrame(data, columns= ['datetime', 'user_id', 'url', 'tweet_content', 'user_name',
                                         'reply_count', 'retweet_count', 'like_count', 'language', 'source'
                                        ])
df = data_frame(tweets_list)

# Bridging a connection with MongoDB Atlas and Creating a new database(twitterscraping) and collections(scraped_data)
client = pymongo.MongoClient("mongodb+srv://jafarhussain:1996@cluster0.4gaz2ol.mongodb.net/?retryWrites=true&w=majority")
db = client.twitterscraping
col = db.scraped_data

# Button 1 - To view the DataFrame
if st.button("View DataFrame"):
    st.success("**:blue[Here is the DataFrame of the Scraped Tweets]**", icon="⬇️")
    st.write(df)
    
# Button 2 - To upload the data to mongoDB database
if st.button("Upload the data to MongoDB"):
    col.delete_many({})   #Deleting old records in the collection
    col.insert_many(df.to_dict('records'))
    st.success('Upload to MongoDB Successful!', icon="✅")

# Converting DataFrame to CSV file
def convert_to_csv(c):
    return c.to_csv().encode('utf-8')

# Converting DataFrame to JSON file
def convert_to_json(j):
    return j.to_json(orient='index')

csv = convert_to_csv(df)
json = convert_to_json(df)

st.success("**:blue[Like to download the data use the below buttons!!!]**",icon="⬇️")

# Button 3 - To download data as CSV
st.download_button(label="Download data as CSV",
                   data=csv,
                   file_name='scraped_tweets_data.csv',
                   mime='text/csv'
                  )

# Button 4 - To download data as JSON
st.download_button(label="Download data as JSON",
                   data=json,
                   file_name='scraped_tweets_data.json',
                   mime='text/csv'
                  )
