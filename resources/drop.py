from flask_restful import Resource
from api import get_tweets, tags, tw_number
from alchemy import db
from logstash import *
import datetime

class DropTweets(Resource):
    def delete(self):
        try:
            db.drop_all()
            elk_logger.warning(gTime() + ' - ' + ': DELETE: <{}> database has been dropped'.format(200))
        except:
            elk_logger.error(gTime() + ' - ' + ': ERROR: <{}> deleting database'.format(500))
            return {'message': 'error dropping database'}, 500

        return {'message': 'database has been dropped'}, 200

    def get(self):
        try:
            db.create_all()
            get_tweets(tw_number, tags)
            elk_logger.info(gTime() + ' - ' + ': SUCCESS: <{}> database has been restored'.format(200))
        except:
            elk_logger.error(gTime() + ' - ' + ': ERROR: <{}> restoring database'.format(500))
            return {'message': 'error restoring database'}, 500
        
        return {'message': 'database has been restored'}, 200