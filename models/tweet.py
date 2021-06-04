from alchemy import db

class TweetModel(db.Model):
    __tablename__ = 'tweets'

    id          = db.Column(db.Integer, primary_key=True)
    tweet       = db.Column(db.String)
    author      = db.Column(db.String)
    followers   = db.Column(db.Integer)
    created     = db.Column(db.String)
    lang        = db.Column(db.String)
    country     = db.Column(db.String)
    rash        = db.Column(db.String)

    def __init__(self, tweet, author, followers, created, lang, country, rash):
        self.tweet      = tweet
        self.author     = author
        self.followers  = followers
        self.created    = created
        self.lang       = lang
        self.country    = country
        self.rash       = rash
    
    def json(self):
        return {
            'tweet':        self.tweet,
            'author':       self.author,
            'followers':    self.followers,
            'created':         self.created,
            'lang':         self.lang,
            'country':      self.country,
            'rash':         self.rash
        }
    
    def save_tweet(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
