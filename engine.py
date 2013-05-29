import twitter

from Analysis.googlebooks import GoogleBooks
from config import twitter_config
from goodreads import GoodReads
from Analysis import Burstiness
from models import Book

class RecommendationService:
	def __init__(self):
		self.goodreads = GoodReads()
		self.googlebooks = GoogleBooks()


	# DEPRECATED
	def recommend_book_by_tweets(self, tweets):
		""" Placeholder function for Tina's code """
		# TODO: Implemen
		return Book(
			title="The Great Gatsby",
			author="F. Scott Fitzgerald",
			image="http://ecx.images-amazon.com/images/I/51SyWimt1SL._BO2,204,203,200_PIsitb-sticker-arrow-click,TopRight,35,-76_AA300_SH20_OU01_.jpg",
			quote="I like large parties, they're so intimate. At small parties, there isn't privacy.",
			link="http://www.amazon.com/The-Great-Gatsby-Scott-Fitzgerald/dp/0743273567"
		)
	
	
	def recommend_book(self, tweet):
		print tweet.text
		keyword = Burstiness.findTweetTopic(tweet.text)
		book_info = self.get_quotes_by_keyword(keyword)
		return book_info
		#return self.get_book_excerpt_by_book_info(book_info)    -- we dont need this for now... the excerpts that were getting returned were not really useable for display

	def get_book_excerpt_by_book_info(self, book_info):
		# Feed in get_quotes_by_keyword output into this method
		return self.googlebooks.get_excerpt(book_info)


	def get_quotes_by_keyword(self, keyword):
		return self.goodreads.book_quotes_by_tag(keyword)


	# DEPRECATED
	def get_book_hardcoded(self, handle):
		if handle == 'ruselprocal':
			return Book(
				title="The Great Gatsby",
				author="F. Scott Fitzgerald",
				image="http://ecx.images-amazon.com/images/I/51SyWimt1SL._BO2,204,203,200_PIsitb-sticker-arrow-click,TopRight,35,-76_AA300_SH20_OU01_.jpg",
				quote="I like large parties, they're so intimate. At small parties, there isn't privacy.",
				link="http://www.amazon.com/The-Great-Gatsby-Scott-Fitzgerald/dp/0743273567"
			)
		if handle == 'kane':
			return Book(
				title="Fahrenheit 451",
				author="Ray Bradbury",
				image="http://bks1.books.google.com/books?id=Shsqc7sd_QoC&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE70GQwVYrQpJbvfosyB4OlGx4zBgjTfdKrnTaR4LYbBXRpcGu4ilWKw6YJgsHTRZ7C8VEB0tcdLOzRhtNjPDPe3Bvey5-8i2T1WoO4uNY2l8IwpkaXBIHxsXEJ_5SPbruJBBcgP6",
				quote="Our civilization is flinging itself to pieces. Stand back from the centrifuge.",
				link="http://www.amazon.com/Fahrenheit-451-Novel-Ray-Bradbury/dp/1451673310"
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
