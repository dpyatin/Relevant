from models import Book, Tweet

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

	def set_handle(self, handle):
		self.handle = handle

	def retrieve_tweets(self):
		# TODO: Implement
		tweet = Tweet(
			user=self.handle,
			tweet="Hello World!",
			timestamp="May 18, 2013 12:03:47",
			retweet_count=5,
			fav_count=3,
			reply_count=2
		)