from time import sleep
import tweepy
import time

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

post_tweet("" )

search = 'Nft'
nrTweets = 25

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
upload_media("", "")
time.sleep(240)

search = 'Nft'
nrTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(120)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break      
