# Chihuahua Bot
A very basic bot to post Chihuahua pictures from reddit to twitter.

## Download the Dependencies 
Install all the needed packages:

```bash
pip install -r requirements.txt
```
## Get your Twitter tokens
- [ ] Go to : https://developer.twitter.com/en/portal/projects-and-apps
- [ ] Create an app
- [ ] Generate your API Key and API Secret.
- [ ] Generate your Access Token and Access Secret.

Tadaa, you're done with Twitter :tada:

> **_NOTE:_** CONSUMER_KEY is the API KEY and CONSUMER_SECRET is the API Secret.

## Get your Reddit tokens
- [ ] Go to : https://www.reddit.com/prefs/apps/
- [ ] Create an app
- [ ] Get your Client ID and Client Secret.

Tadaa, you're done with Reddit too :tada:
> **_NOTE:_** You can find your Client ID right under wep app.

Put all your tokens in your .env file as follows:
```
CONSUMER_KEY = "Your API KEY" 
CONSUMER_SECRET = "Your API SECRET"
ACCESS_KEY = "Your Access Key"
ACCESS_SECRET = "Your Access Secret"

CLIENT_ID = 'Your Client ID'
CLIENT_SECRET = 'Your Client Secret'
```

Congrats :balloon:! You're all set to run your bot :robot:! You may want to customize it (change subreddit, delay between each tweet...)

For more help check:
- Praw: https://praw.readthedocs.io/
- Tweepy: http://docs.tweepy.org/
- Bonus : https://www.youtube.com/watch?v=y654TxcRuL0
