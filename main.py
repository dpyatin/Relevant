from engine import RecommendationService, TwitterService
from flask import Flask, request, jsonify
from models import Tweet, Book
app = Flask(__name__)

@app.route("/")
def index():
	return "NYC Publishing Hackathon: Relevant"

@app.route("/api/getBookRecommendation/", methods=['GET', 'POST'])
def get_book_recommendation():
	twitter_handle = _getParameter('twitterHandle')
	if twitter_handle is None:
		return _error("Missing required parameter: twitterHandle")

	# TODO: Try/Catch
	twitter_service = TwitterService(twitter_handle)
	tweets = twitter_service.retrieve_tweets()

	reco_service = RecommendationService()
	recommendation = reco_service.recommend_book_by_tweets(tweets)

	return jsonify(recommendation.__dict__)

def _getParameter(parameter):
	if parameter in request.form:
		return request.form[parameter]
	if parameter in request.args:
		return request.args[parameter]

	return None

def _success(message):
	return jsonify(success=message)

def _error(message):
	return jsonify(error=message)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)