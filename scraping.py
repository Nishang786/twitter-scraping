import tweepy
from tweepy.api import API
from tweepy.binder import bind_api
import logging
consumer_key = 'I4dAcf2EuoNOL41aoEdMzPhTL'
consumer_secret = 'pIfst3OLbBNDwigBMjpkqMjMTEIAyjG9AF79GlR9vb06k9ikXK'
access_token = '1310946692397764620-JhNEgW3OW4g2wCMWNvdzwNxGic4EfB'
access_secret = 'jAirddJvqNtw6VzZXGcnGgC0CalydQvIrDHxlCBwhkvSB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
my_tweets = api.user_timeline('')
for t in my_tweets:
    print(t.text)