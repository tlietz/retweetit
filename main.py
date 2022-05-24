import tweepy

from client_secrets import *

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
query = 'news'
tweets = client.search_recent_tweets(query=query, max_results=10)
print(tweets.data[0])
