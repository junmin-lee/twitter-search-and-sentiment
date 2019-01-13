
import os
import tweepy
from textblob import TextBlob
import csv

#Twitter Key and token configuration
#Don't forget to restart the termial when after setting environment variables
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key_secret = os.environ.get('CONSUMER_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

#Create authentication variable
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)

#Create main variable
api = tweepy.API(auth)

#Get an string input from user
search_word = input('Enter search word: ')
public_tweets = api.search(q=search_word) 
# Prepare to write csv file as an output
tweet_file = open('tweet_output.csv','w',encoding='utf-8',newline='')

for tweet in public_tweets:
    #tweets to go in the first colomn
    tweet_content = tweet.text
    #positive/negative label for second colomn, score calculation -1~1
    analysis = TextBlob(tweet.text)
    tweet_score = analysis.sentiment.polarity * analysis.sentiment.subjectivity
    label = ''
    if tweet_score < 0:
        label = 'Negative'
    else:
        label = 'Positive'
    #Print the tweets and get the sentiments
    write_row = csv.writer(tweet_file)
    write_row.writerow([tweet_content, label])

tweet_file.close()
