import tweepy
from textblob import TextBlob

consumer_key = 'mvA8hYDHjlF2K4HglAEhf7odP'
consumer_secret = 'smPrEvaqg93SwCB3PA1yqYMwNjnt8ba5W626BBW8AWWTIUvfQW' 

access_token = '27921373-Zgr5vw7RPm2ZfW8rX2ruwugSSGBIz3ySND8SbVnsc'
access_token_secret = 'q3jPmkpnYBF4HlfmX0xMdouNowONSWsiq8TFwDywFQMtp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

action = raw_input("Type a word to analyze the sentiments of tweeters. > ")
public_tweets = api.search(action)

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	print(tweet.text, analysis.sentiment)