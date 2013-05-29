import csv as csv 
from operator import itemgetter
from nltk.stem.wordnet import WordNetLemmatizer
import re
import sys
import nltk.data, nltk.tag
from nltk.corpus import stopwords
import time

def removeSpecialTokens(cur_line):
	cur_tokens = cur_line.replace('\\n',' ').split(' ')
	rs_tokens = []

	for tk in cur_tokens:
		if tk == None or len(tk) == 0:
			continue

		if tk == 'RT' or tk[0] == '@' or tk[0] == '\\':
			continue
		else:
			rs_tokens.append(tk)
	

	return ' '.join(rs_tokens)

def findTweetTopic(tweet): 
	#tagger = nltk.data.load(nltk.tag._POS_TAGGER)
	tokenized = nltk.wordpunct_tokenize(tweet)

	# remove stopwords
	filtered_words = [w for w in tokenized if not w in stopwords.words('english')]

	# identify parts of speech, pull out nouns
	taggedTweet = nltk.pos_tag(filtered_words)
	
	nouns = []
	for word in taggedTweet:
		if(word[1] == "NN" or word[1] == "FW" or  word[1] == "NNS" or word[1] == "NNP" or word[1] == "NNPS"):
			word = str(word[0])
			lmtzr = WordNetLemmatizer()
			word = lmtzr.lemmatize(word)
			nouns.append([word, 0, 0, 0.0])

	return nouns


'''
Processes the corpus into a readable format.
'''
def processCorpus(csvfile):
	csv_file_object = csv.reader(open('G:\\Users\\Russell\\Dropbox\\PubHack\\timelinecorpus.csv', 'r')) 

	myCorpus = []
	rowCount = 0

	f_write = open('cleancorpus.txt','w')


	for row in csv_file_object:
		document = ''
		for tweet in row:
			if tweet == '':
				continue
			document += removeSpecialTokens(tweet.lstrip('\'\"[').split('\',')[0].split('\",')[0]) + ' '
		myCorpus.append(document)
		print>>f_write, document

	return myCorpus

def bursty(text):
	#process the corpus
	#myCorpus = processCorpus('timelinecorpus.csv')
	
	if text == '':
		print "Please input text"
		text = sys.stdin.readline()
	
	tstart = time.clock()
		
	#pick up existing corpus
	myCorpus = open('cleancorpus.txt','rb')
		
	#stdin version
	nouns = findTweetTopic(text)
		
	for row in myCorpus:
		for i in range(0, len(nouns)):
			targetNoun1 = ' ' + str(nouns[i][0]) + ' ' 
			targetNoun2 = ' ' + str(nouns[i][0]) + ','
			targetNoun3 = ' ' + str(nouns[i][0]) + '.'
			findKeys1 = [m.start() for m in re.finditer(targetNoun1, row)]
			findKeys2 = [m.start() for m in re.finditer(targetNoun2, row)]
			findKeys3 = [m.start() for m in re.finditer(targetNoun3, row)]    	
			if(len(findKeys1) + len(findKeys2) + len(findKeys3) > 0):
				nouns[i][1] = nouns[i][1] + len(findKeys1) + len(findKeys2) + len(findKeys3)
				nouns[i][2] = nouns[i][2] + 1

	for obj in nouns:
		if obj[2] > 0:
			obj[3] = float(float(obj[1]) / float(obj[2]))
		else:
			obj[3] = 0
	nouns = sorted(nouns, key=itemgetter(3), reverse=True)
	
	tfin = time.clock() - tstart
	print "Time:" + str(tfin)
	
	print nouns
	return nouns[0][0]

if __name__ == "__main__":
	bursty('')

