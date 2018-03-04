import tweepy
from textblob import TextBlob

consumer_key = 'm88Ti1LsNEg5siKhgzdMaoefm'
consumer_secret = 'MmKnrZFGtGCTA5pLhqZaxGOAjYOGEppooKh4iOPL0q5kVjhsf9'

access_token = '830092531983609856-LkEDKXmFkVKWDKsg87hBOUlUjX9h4gd'
access_token_secret =  'XXoaIHNqRr6KMiTsGoOfR1jukF9z4kTb6GWNNPz4AbQDh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweet = api.search(raw_input())

print("Do you want to read all tweets?   yes/no")
a=raw_input()
if a=='yes':
	for tweet in public_tweet:	
		print(tweet.text)
		print(TextBlob(tweet.text).sentiment)
		print(" ")
else:
	for tweet in public_tweet:
	        print(TextBlob(tweet.text).sentiment)
