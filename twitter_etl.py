import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import config

def run_twitter_etl():
	# Twitter authentication // Autenticando no Twitter
	auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
	auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
	
	# Creating an API object // Criando um objeto API
	api = tweepy.API(auth)
	tweets = api.user_timeline(screen_name='@saifedean',
		count=2,
 		include_rts=False,
 		tweet_mode='extended'
 	)

twitter_list = []

for tweet in tweets:
 	refined_tweet = {"user": tweet.user.screen_name,
 	"text": tweet.full_text,
 	"favorite_count": tweet.favorite_count,
 	"created_at": tweet.created_at,
 	"location": tweet.user.location
 	}
 	#tweet = tweet._json["full_text"]

 	twitter_list.append(refined_tweet)

df = pd.DataFrame(twitter_list)
df.to_csv("refined_tweets.csv")