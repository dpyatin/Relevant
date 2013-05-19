import twitter

from config import twitter_config
from models import Book

class RecommendationService:
	def __init__(self):
		pass

	def recommend_book_by_tweets(self, tweets):
		""" Placeholder function for Tina's code """
		# TODO: Implement
		return Book(
			title="The Great Gatsby",
			author="F. Scott Fitzgerald",
			image="http://ecx.images-amazon.com/images/I/51SyWimt1SL._BO2,204,203,200_PIsitb-sticker-arrow-click,TopRight,35,-76_AA300_SH20_OU01_.jpg",
			quote="The Great Gatsby is one of the great classics of twentieth-century literature.",
			link="http://www.amazon.com/The-Great-Gatsby-Scott-Fitzgerald/dp/0743273567"
		)


class TwitterService:
	def __init__(self, handle):
		self.handle = handle
		self.twitter = None

	def set_handle(self, handle):
		self.handle = handle

	def authenticate(self):
		self.twitter = twitter.Api(**twitter_config)

	def get_tweets(self):
		if not self.twitter:
			self.authenticate()

		if not self.handle:
			raise Exception('Parameter `handle` not defined in the engine')

		return self.twitter.GetUserTimeline(self.handle)
