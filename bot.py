import tweepy
import time

consumer_key = 'Your_Consumer_Key'
consumer_secret = 'Your_Consumer_Secret_Key'

key = 'Your_Access_Token'
secret = 'Your_Access_Secret_Token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Any_Search_text'
nrt = 50

for tweet in tweepy.Cursor(api.search, search).items(nrt):
    try:
        print('Tweet Liked.')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
