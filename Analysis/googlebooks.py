from apiclient.discovery import build
# from googlebooks import GoogleBooks; gb = GoogleBooks(); gb.getExcerpt({'quote': 'politics', 'title': 'kennedy'})
class GoogleBooks:
	api_key = "AIzaSyAnwBRAP94niYqybkY8QkAIvG7QqbDiicQ"

	def getExcerpt(self, book_info):
		book_result = {}

		response = self._search_book(book_info)

		for book in response.get('items', []):
			book_result = self._parse_book(book)

			if book_result is not None:
				book_result['link'] += '&q=' + book_info['quote']
				return book_result

		return book_result


	def _search_book(self, book_info):
		""" Queries Google Books based on Book Info
		In particular it looks at the quote and book title
		"""
		response = []

		try:
			service = build('books', 'v1', developerKey=self.api_key)

			query = {
				'source': 'public',
				'q': book_info['quote'] + "+intitle:" + book_info['title'] }

			request = service.volumes().list(**query)
			request.uri += "&country=US" # Hack
			response = request.execute()
		except:
			pass

		return response


	def _parse_book(self, book):
		""" Parses Title, Author and Excerpt from Google Book API Call
		Returns dict with {title, author, excerpt}
		"""

		result = None
		try:
			title = book['volumeInfo']['title']
			title = title.encode('ascii', 'ignore')

			author = book['volumeInfo']['authors'][0]
			author = author.encode('ascii', 'ignore')

			excerpt = book['searchInfo']['textSnippet']
			excerpt = excerpt.encode('ascii', 'ignore')

			link = book['accessInfo']['webReaderLink']
			link = link.encode('ascii', 'ignore')
			
			result = {
				'title': title,
				'author': author,
				'excerpt': excerpt,
				'link': link }
		except:
			pass

		return result
