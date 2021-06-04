from flask_restful import Resource, reqparse
from models.tweet import TweetModel
from logstash import *
import sqlite3

path = reqparse.RequestParser()
path.add_argument('order_by_followers_desc', type=int)

class Tweets(Resource):
    def get(self):
        conn = sqlite3.connect('twitter.db')
        sql  = conn.cursor()

        params          = path.parse_args()
        valid_params    = {key:params[key] for key in params if params[key] is not None}
        
        if valid_params.get('order_by_followers_desc'):

            param = valid_params.get('order_by_followers_desc')
            
            search = "SELECT * FROM (SELECT *, RANK () OVER (ORDER BY followers DESC) FROM tweets ) limit ?"
            tpl    = tuple([valid_params[key] for key in params])

            try:
                resp   = sql.execute(search, tpl)
                elk_logger.info(gTime() + ' - ' + ': SUCCESS: <{}> GET/tweets?order_by_followers_desc=?'.format(200))
            except:
                elk_logger.error(gTime() + ' - ' + ': ERROR: <{}> running query: {}'.format(500, search))
                return {'message': 'query error'}, 500

            tweet = []
            for tw in resp:
                tweet.append({
                    'author':       tw[2],
                    'followers':    tw[3]
                })

            return {'authors': tweet}, 200
        
        elk_logger.info(gTime() + ' - ' + ': SUCCESS: <{}> GET/tweets'.format(200))
        return {'tweets': [tweet.json() for tweet in TweetModel.query.all()]}, 200