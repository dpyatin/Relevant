from bs4 import BeautifulSoup

import urllib

class GoodReads:
	quote_url = "http://www.goodreads.com/quotes/tag?utf8=%E2%9C%93&id=[TAG]"


	def book_quotes_by_tag(self, tag):
		""" Quotes by Tag
		Scrapes the first page of quotes for a given tag and strips
		any quotes that don't have a book associated with them.
		Returns a dict with {quote, author, book}.
		"""
		url = self.quote_url.replace("[TAG]", tag)
		html = self._fetch_page(url)
		quotes = self._parse_quotes(html)

		return quotes


	def _fetch_page(self, url):
		""" HTTP GET Request to URL
		Returns the HTML of the page
		"""

		html = ""
		try:
			request = urllib.urlopen(url)
			html = request.read()
		except:
			pass

		return html


	def _parse_quotes(self, html):
		""" Parses Quotes out of GoodReads HTML
		Returns a dict with {quote, author, image, title, tags}.
		"""
		quotes = []

		soup = BeautifulSoup(html)
		quote_list = soup.find_all("div", "quote")
		for quote in quote_list:
			# Extract Quote, Author, Image, Title, Tags from each <div>
			try:
				quotation = quote.find("div", "quoteText").get_text()
				quotation = quotation.split(u'\u201c')[1]
				quotation = quotation.split(u'\u201d')[0]
				quotation = quotation.encode("ascii", "ignore")

				author = quote.find("img").attrs["alt"]
				author = author.encode("ascii", "ignore")

				image = quote.find("img").attrs["src"]
				image = image.encode("ascii", "ignore")

				title = quote.find("i").get_text().strip()
				title = title.encode("ascii", "ignore")

				tags = quote.find("div", "greyText").find_all("a")
				tags = [tag.get_text() for tag in tags]
				tags = [tag.encode("ascii", "ignore") for tag in tags]

				quotes.append({
					'quote': quotation,
					'author': author,
					'image': image,
					'title': title,
					'tags': tags })
			except:
				pass

		return quotes
