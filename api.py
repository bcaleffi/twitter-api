import tweepy 
import os
from models.tweet import TweetModel

consumer_key            = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret         = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token            = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret     = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tags = {"#openbanking", "#remediation", "#devops", "#sre", "#microservices", "#observability", "#oauth", "#metrics", "#logmonitoring", "#opentracing"}
tw_number = 100

def get_tweets(twn, tags):
    for tg in tags:
        resp = tweepy.Cursor(api.search, q=tg, tweet_mode="extended").items(twn)
        for i in resp:
            tweet_data = {
                "tweet":        i.full_text,
                "author":       i.author.name,
                "followers":    i.author.followers_count,
                "created":      i.created_at,
                "lang":         i.lang,
                "country":      i.geo,
                "rash":         tg
            }
            tweet = TweetModel(**tweet_data)
            try: 
                tweet.save_tweet()
            except:
                return {'message': 'Internal error occured trying to access SQLite'}, 500
            

    
