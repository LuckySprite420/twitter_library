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

@app.task(daily.after("10:00"))
def do_daily_after_ten():
    print("good morning")

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

post_tweet("Good morning web3!!! #NFTs #NFTCommumity #Solana #warland #Metaverse #NFTartists #NFTart" )

if __name__ == "__main__":
        app.run()