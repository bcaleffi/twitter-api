from flask import Flask, render_template
from flask_restful import Api
from resources.tweet import Tweets
from resources.hourly import TweetsHour
from resources.tags import Tags
from resources.drop import DropTweets
from api import get_tweets, tags, tw_number
from prometheus_flask_exporter import PrometheusMetrics
from alchemy import db
from logstash import *

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']           = 'sqlite:///twitter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']    = False
db.init_app(app)
metrics = PrometheusMetrics(app)

@app.before_first_request
def create_database():
    db.create_all()
    get_tweets(tw_number, tags)

api.add_resource(Tweets, '/tweets')
api.add_resource(TweetsHour, '/tweets_per_hour')
api.add_resource(Tags, '/tweets_per_tag')
api.add_resource(DropTweets, '/database')

if __name__ == '__main__':
    app.run()