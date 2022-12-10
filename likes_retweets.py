import asyncio
from rocketry import Rocketry
from rocketry.conds import every
from rocketry.conds import hourly, daily, weekly 
from rocketry.conds import time_of_day
from rocketry.conds import cron
from rocketry.conds import daily, time_of_week
from pathlib import Path
import time
from time import sleep
import tweepy

app = Rocketry(config={'task_execution': 'async'})

@app.task(daily.after("15:00"))
def do_daily_after_fifteen():
    print("Done")

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
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'NFT'
nrTweets = 60

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(120)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     
    
search = 'Crypto'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'Crypto'
nrTweets = 60

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(120)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     
    
search = 'Metaverse'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweeted')
        tweet.retweet()
        time.sleep(100)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

search = 'Metaverse'
nrTweets = 60

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(120)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break     

if __name__ == "__main__":
        app.run()