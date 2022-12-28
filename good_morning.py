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

post_tweet("Good morning web3!!! #NFTs #NFTCommumity #Solana #warland #Metaverse #NFTartists #NFTart" )

print('Done! I am a good bot!')

#you can use cronjob to run this script everyday