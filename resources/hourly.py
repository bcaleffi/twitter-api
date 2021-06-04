from flask_restful import Resource
from models.tweet import TweetModel
from logstash import *
import sqlite3

class TweetsHour(Resource):
    def get(self):
        
        conn = sqlite3.connect('twitter.db')
        sql  = conn.cursor()

        search = "SELECT COUNT(*),strftime ('%H',created) hour FROM tweets GROUP BY strftime ('%H',created)"
        try: 
            resp   = sql.execute(search)
            elk_logger.info(gTime() + ' - ' + ': SUCCESS: <{}> GET/tweets_per_hour'.format(200))
        except:
            elk_logger.error(gTime() + ' - ' + ': ERROR: <{}> running query: {}'.format(500, search))
            return {'message': 'query error'}, 500

        tweet = []
        for tw in resp:
            tweet.append({
                'tweets':   tw[0],
                'at_hour':     tw[1]+":00"
            })

        return {'tweets_per_hour': tweet}, 200


