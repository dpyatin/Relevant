class Book:
	def __init__(self, title, author, image, quote, link=None):
		self.title = title
		self.author = author
		self.image = image
		self.quote = quote
		self.link = link

	def __repr__(self):
		return "%s, %s" % (self.title, self.author)