import csv as csv 
import numpy as np
import nltk as nltk
from operator import itemgetter
import globals
from nltk.stem.wordnet import WordNetLemmatizer
import TweetExtraction
import re
import sys
import nltk.data, nltk.tag
from nltk.corpus import stopwords
import pytumblr
from sklearn.ensemble import RandomForestClassifier 

def findTweetTopic(): 
	tagger = nltk.data.load(nltk.tag._POS_TAGGER)

	inBuffer = []
	tweet = sys.stdin.readline()

	tokenized = nltk.wordpunct_tokenize(tweet)

	#remove stopwords
	filtered_words = [w for w in tokenized if not w in nltk.corpus.stopwords.words('english')]

	#identify parts of speech, pull out nouns
	taggedTweet = nltk.pos_tag(filtered_words)


	nouns = []
	for word in taggedTweet:
		if(word[1]=="NN" or word[1]=="FW" or  word[1] == "NNS" or word[1]== "NNP" or word[1]=="NNPS"):
			word = str(word[0])
			lmtzr = WordNetLemmatizer()
			word = lmtzr.lemmatize(word)
			nouns.append([word, 0, 0, 0.0])
	csv_file_object = csv.reader(open('tumblrMaster.csv', 'rU')) 

	myCorpus = []
	rowCount=0
	wordCount=0


	for row in csv_file_object:
	    row = ' '.join(row)
	    row = str(row)
	    myCorpus.append(row)

	    for i in range(0, len(nouns)):

	    	targetNoun1 = ' ' + str(nouns[i][0]) + ' ' 
	    	targetNoun2 = ' ' + str(nouns[i][0]) + ','
	    	targetNoun3 = ' ' + str(nouns[i][0]) + '.'
	    	findKeys1 = [m.start() for m in re.finditer(targetNoun1, row)]
	    	findKeys2 = [m.start() for m in re.finditer(targetNoun2, row)]
	    	findKeys3 = [m.start() for m in re.finditer(targetNoun3, row)]    	
	    	if(len(findKeys1)+len(findKeys2)+len(findKeys3)>0):
	    		nouns[i][1]= nouns[i][1]+len(findKeys1)+len(findKeys2)+len(findKeys3)
	    		nouns[i][2]= nouns[i][2] + 1

	for obj in nouns:
		if obj[2]>0:
			obj[3] = float(float(obj[1])/float(obj[2]))
		else:
			obj[3] = 0
	nouns= sorted(nouns, key=itemgetter(3), reverse=True)
	print nouns
	return nouns[0][0]

print findTweetTopic()
