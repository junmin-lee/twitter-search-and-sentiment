
#Don't forget to restart the termial when after setting environment varaibles

import os
import tweepy
from textblob import TextBlob

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key_secret = os.environ.get('CONSUMER_KEY_SECRET')

access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

#Create authentication variable
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)

#Create main variable
api = tweepy.API(auth)

#Search
public_tweets = api.search('Trump')

#Print the tweets and get the sentiments
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
