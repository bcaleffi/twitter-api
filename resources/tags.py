from flask_restful import Resource
from models.tweet import TweetModel
from logstash import *
import sqlite3
import operator
import itertools

class Tags(Resource):
    def get(self):
        
        conn = sqlite3.connect('twitter.db')
        sql  = conn.cursor()
        
        search = "SELECT rash, lang, COUNT(*) FROM tweets GROUP BY rash, lang"

        try:
            resp        = sql.execute(search)
            elk_logger.info(gTime() + ' - ' + ': SUCCESS: <{}> GET/tweets_per_tag'.format(200))
        except:
            elk_logger.error(gTime() + ' - ' + ': ERROR: <{}> running query: {}'.format(500, search))
            return {'message': 'query error'}, 500

        tweet = []
        for tw in resp:
            tweet.append({
                'rash':      tw[0],
                'lang':      tw[1],
                'tweets':    tw[2]
            })
        
        tweet_out=[]
        for i,g in itertools.groupby(tweet, key=operator.itemgetter("rash")):
            tweet_out.append(list(g))

        return {'tweets_per_tags': tweet_out}, 200