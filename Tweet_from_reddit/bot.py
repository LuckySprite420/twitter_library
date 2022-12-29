from glob import glob
import urllib
import os
import time
import requests
import tweepy
import praw
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

reddit = praw.Reddit(
                        user_agent='reddit Twitter tool monitoring ',
                        client_id="",
                        client_secret="")

IMAGE_DIR = 'Images'

POSTED_CACHE = 'posted_posts.txt'

TWEET_SUFFIX = ' #news #meme #fun #lmao #metaverse #games #mmorpg #nft #nftart #playtoearn'

DELAY_BETWEEN_TWEETS = 86400  # a day



def tweet():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    for submission in reddit.subreddit('cryptocurrencymemes').top():
        post_dict = tweet_creator(submission)
        for post in post_dict:
            img_path = post_dict[post]['img_path']
            extra_text = ' ' + post_dict[post]['link'] + TWEET_SUFFIX
            extra_text_len = 1 + 24 + len(TWEET_SUFFIX)
            if img_path:  # Image counts as a link
                extra_text_len += 24
            post_text = strip_title(post, 280 - extra_text_len) + extra_text
            if img_path:
                api.update_status_with_media(filename=img_path, status=post_text)
            else:
                api.update_status(status=post_text)

            time.sleep(DELAY_BETWEEN_TWEETS)

def tweet_creator(submission):
    post_dict = {}
    post_ids = []
    if not already_tweeted(submission.id) and get_image(submission.url) != '' and 'jpg' in get_image(
                submission.url):
        post_dict[submission.title] = {}
        post = post_dict[submission.title]
        post['link'] = submission.url
        post['img_path'] = get_image(submission.url)
        post_ids.append(submission.id)
        f = open(POSTED_CACHE, "a")
        f.write(submission.id + "\n")
        f.close()
    else:
        print("Already tweeted or it's not an image.")
    return post_dict


def already_tweeted(post_id):
    ''' Checks if the reddit post has already been tweeted '''
    found = False
    with open(POSTED_CACHE, 'r') as in_file:
        for line in in_file:
            if post_id in line:
                found = True
                break
    return found

def get_image(img_url):
    if 'jpg' in img_url:
        file_name = os.path.basename(urllib.parse.urlsplit(img_url).path)
        img_path = IMAGE_DIR + '/' + file_name
        print('[bot] Downloading image at URL ' + img_url + ' to ' + img_path)
        resp = requests.get(img_url, stream=True)
        if resp.status_code == 200:
            with open(img_path, 'wb') as image_file:
                for chunk in resp:
                    image_file.write(chunk)
            return img_path
    else:
        print("It's not an image")
    return ''

def strip_title(title, num_characters):
    if len(title) <= num_characters:
        return title
    else:
        return title[:num_characters - 1] + '…'

def main():
    if not os.path.exists(POSTED_CACHE):
        with open(POSTED_CACHE, 'w'):
            pass
        if not os.path.exists(IMAGE_DIR):
            os.makedirs(IMAGE_DIR)

    tweet()
    # To clean out the image cache
    for filename in glob(IMAGE_DIR + '/*'):
        os.remove(filename)

if __name__ == '__main__':
    main()
