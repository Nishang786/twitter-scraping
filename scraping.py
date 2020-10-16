import tweepy
from tweepy.api import API
from tweepy.binder import bind_api
import logging
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
my_tweets = api.user_timeline('')
for t in my_tweets:
    print(t.text)
