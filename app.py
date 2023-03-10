import pandas as pd
import streamlit as st
import snscrape.modules.twitter as sntwitter

st.header('Cyberbullying Detection')
# scrape tweets
def scrape_tweets(field, n):
    tweet_list = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(field).get_items()):
        if i > n:
            break
        tweet_list.append([tweet.content])
    return tweet_list

with st.sidebar:
    n = st.slider('Number of posts to scrape', 1, 1000, 100)
    field = st.text_input('Enter text to search for', 'cyberbullying')
    

df = pd.DataFrame(scrape_tweets(field, n), columns=['tweets'])
st.dataframe(df)
st.download_button(label='Download', data=df.to_csv(index=False), file_name='tweets.csv', mime='text/csv')
    

