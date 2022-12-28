import tweepy
import time
from time import sleep

#Instalation / Access to Twitter account
consumer_key = ""
consumer_secret = ""
bearer_token = r''
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

def post_tweet(text):
    api.update_status(text)
    
def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

search = 'NFT'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'NFT'
nrTweets = 30

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     
    
search = 'Crypto'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'Crypto'
nrTweets = 30

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     
    
search = 'Metaverse'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'Metaverse'
nrTweets = 30

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    
search = 'playtoearn'
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'playtoearn'
nrTweets = 30

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(80)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     
