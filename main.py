import os
import sys

from engine import RecommendationService, TwitterService
from flask import Flask, request, jsonify
from models import Book

app = Flask(__name__)

@app.route("/")
def index():
	return "NYC Publishing Hackathon: Relevant"

@app.route("/api/getBookRecommendation/", methods=['GET', 'POST'])
def get_book_recommendation():
	twitter_handle = _getParameter('twitterHandle')
	if twitter_handle is None:
		return json_error("Missing required parameter: twitterHandle")

	try:
		twitter_service = TwitterService(twitter_handle)
		twitter_service.authenticate()
		tweets = twitter_service.get_tweets()

		reco_service = RecommendationService()
		recommendation = reco_service.recommend_book_by_tweets(tweets)

		# Demo Time! (TODO: Remove this)
		if twitter_handle in ['ruselprocal', 'kane']:
			recommendation = reco_service.get_book_hardcoded(twitter_handle)
		
	except:
		return json_error("%s %s" % sys.exc_info()[:2])

	return json_success(recommendation.__dict__)

def json_success(message):
	return jsonify(message)

def json_error(message):
	return jsonify(error=message)

def _getParameter(parameter):
	if parameter in request.form:
		return request.form[parameter]
	if parameter in request.args:
		return request.args[parameter]

	return None

if __name__ == "__main__":
	# Heroku default port is 33507, defined in an environment variable
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)