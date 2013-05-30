import os
import sys

from engine import RecommendationService, TwitterService
from flask import Flask, request, jsonify
from app import db
import models

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

		tweet_list = [tweet.__dict__ for tweet in tweets]

		for tweet in tweet_list:
			try:
				tweet['_user'] = tweet['_user'].__dict__
			except KeyError:
				pass
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
		latestTweet = tweets[0]
		reco_service = RecommendationService()
		recommendation = reco_service.recommend_book(latestTweet)
		
		user = models.User.query.filter_by(username=twitter_handle).first()
		if(user):
			print "Tweet retrieved from the database for the user : " + user.lastTweet
			user.lastTweet = latestTweet.text
			#db.session.merge(user)
			db.session.commit()
		else:
			user = models.User()
			user.username = twitter_handle
			user.lastTweet = latestTweet.text
			print "Saving new user with the following tweet : " + user.lastTweet
			db.session.add(user)
			db.session.commit()
			
		# Demo Time! (TODO: Remove this)
		#if twitter_handle in ['ruselprocal', 'kane']:
		#	recommendation = reco_service.get_book_hardcoded(twitter_handle)

	except:
		return json_error("%s %s" % sys.exc_info()[:2])
	
	if(len(recommendation) > 0):
		return json_success(recommendation[0])
	else:
		return jsonify(result="none")

@app.route("/api/areNewTweetsAvailable/", methods=['GET', 'POST'])
def check_for_new_tweets():
	username = _getParameter('username')
	if username is None:
		return json_error("Missing required parameter: username")
	
	try:
		twitter_service = TwitterService(username)
		twitter_service.authenticate()
		tweets = twitter_service.get_tweets()
		user = models.User.query.filter(models.User.username == username).all()
		#print tweets[1].text
		if(user):
			if u.lastTweet == tweets[0].text:
				return jsonify(result="false")
			else:
				reco_service = RecommendationService()
				recommendation = reco_service.recommend_book(tweets[0].text)
				if(len(recommendation) > 0):
					return jsonify(result="true")
				else:
					return jsonify(result="false")
		
		return jsonify(result="true")
	
	except Exception as e:
		raise e #return json_error("%s %s" % sys.exc_info()[:2])

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