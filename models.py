from app import db

class Book:
	def __init__(self, title, author, image, quote, link=None):
		self.title = title
		self.author = author
		self.image = image
		self.quote = quote
		self.link = link

	def __repr__(self):
		return "%s, %s" % (self.title, self.author)
	
class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique=True)
	lastTweet = db.Column(db.String(140))
		
	def __repr__(self):
		return "%s, %s" % (self.username, self.tweet)