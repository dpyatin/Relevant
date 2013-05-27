import os
import sys

from engine import RecommendationService, TwitterService
from flask import Flask, request, jsonify
from models import Book

app = Flask(__name__)

@app.route("/")
def index():
	return "NYC Publishing Hackathon: Relevant"

@app.route("/api/getUserTweets/")
def get_user_tweets():
	twitter_handle = _getParameter('twitterHandle')
	if twitter_handle is None:
		return json_error("Missing required parameter: twitterHandle")

	tweet_json = []
	try:
		twitter_service = TwitterService(twitter_handle)
		twitter_service.authenticate()
		tweets = twitter_service.get_tweets()

		tweet_dict = [tweet.__dict__ for tweet in tweets]
		for tweet in tweet_dict:
			if '_user' in tweet:
				tweet['_user'] = tweet['_user'].__dict__
				tweet_json.append(tweet)
	except:
		return json_error("%s %s" % sys.exc_info()[:2])

	return jsonify(result=tweet_json)

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

@app.route("/api/areNewTweetsAvailable/", methods=['GET', 'POST'])
def check_for_new_tweets():
	username = _getParameter('username')
	if username is None:
		return json_error("Missing required parameter: username")
	
	"""tweet_json=[]
	try:
		twitter_service = TwitterService(username)
		twitter_service.authenticate()
		tweets = twitter_service.get_tweets()
		"""
		# check against database and return result
	return jsonify(result=true)

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