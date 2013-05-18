class Book:
	def __init__(self, title, author, image, quote, link=None):
		self.title = title
		self.author = author
		self.image = image
		self.quote = quote
		self.link = link

	def __repr__(self):
		return "%s, %s" % (self.title, self.author)


class Tweet:
	def __init__(self, user, tweet, timestamp, retweet_count=0, fav_count=0, reply_count=0):
		self.user = user
		self.tweet = tweet
		self.timestamp = timestamp
		self.retweet_count = retweet_count
		self.fav_count = fav_count
		self.reply_count = reply_count

	def __repr__(self):
		return "@%s: %s" % (self.user, self.tweet)