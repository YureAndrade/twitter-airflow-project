import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():

	access_key = ""
	access_secret = ""
	consumer_key = ""
	consumer_secret = ""

	# Twitter authentication // Autenticando no Twitter
	auth = tweepy.OAuthHandler(access_key, access_secret)
	auth.set_access_token(consumer_key, consumer_secret)

	# Creating an API object // Criando um objeto API
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name='@saifedean',
								count=200,
								include_rts=True,
								tweet_mode='extended'
								)

	list = []
	for tweet in tweets:
		tweet = tweet._json["full_text"]

		refined_tweet = {"user": tweet.user.screen.name,
						"text": text,
						"favorite_count": tweet.favorite_count,
						"created_at": tweet.created_at
						}

		list.append(refined_tweet)

	df = pd.DataFrame(list)
	pd.to_csv("refined_tweets.csv")