import tweepy
from textblob import TextBlob 

consumer_key = 'xxxx'
consumer_secret = 'xxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api =tweepy.API(auth)

#search for tweets with name "food"

food_tweets = api.search('food')

for tweet in food_tweets:
	print(tweet.text)
	sentimentAnalysis = TextBlob(tweet.text)
	print(sentimentAnalysis.sentiment)