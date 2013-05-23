import csv as csv 
import numpy as np
import nltk as nltk
import globals

import TweetExtraction
import re
import sys
import nltk.data, nltk.tag
from nltk.corpus import stopwords
import pytumblr
from sklearn.ensemble import RandomForestClassifier 

def makeCorpus():

	consumerKey = "5HbBVA1ZUQxeYDMcC0aeCPlIMTpICD2y5lAYUxVveMo7gN13Bu"

	#start reading in tumblr data
	client = pytumblr.TumblrRestClient(
	    consumerKey,
	    'YllewzlXLwOeLwytOgfGksZbOc8owJvAV6lI2hIXCiGOkcFJMO',
	    '',
	    '',
	)


	#read in list of top 1000 tumblr accounts
	readMaster  = open('userNamesMaster.txt', 'rU')  
	open_file_object = csv.writer(open("tumblrMaster.csv", "wb"))

	while(readMaster.readline()):
		
		userCorpus = []

		#clean up user's tumblr posts and add to corpus
		row = readMaster.readline()
		locNewLine = int(row.find('\n'))
		row = row[0:locNewLine]
		print row 
		try:
			posts = client.posts(row, filter='text')['posts']
		except KeyError:
			pass
		for x in posts:
			if(x['type']=='text'):
				postRev = x['body'].encode('ascii', 'ignore')
				postRev = re.sub('\n', ' ', postRev)
				userCorpus.append(postRev)
			if(x['type']=='photo' and x['caption']!= ''):
				postRev = x['caption'].encode('ascii', 'ignore')
				postRev = re.sub('\n', ' ', postRev)
				userCorpus.append(postRev)
		open_file_object.writerow(userCorpus)

'''
	with open ("tumblrs.txt", "r") as myfile:
	   data=myfile.read().replace('\n', '')


	user_write = open('userNames3.txt', 'w')

	userNames = []
	startInds =  [m.start() for m in re.finditer('href=', data)]
	size = 0
	for ind in startInds:
		len = 0
		while(data[len+ind]!=' '):
			len = len + 1
		curUser = data[ind+13:ind+len]
		x = int(curUser.find('.'))
		curUser = curUser[0: x]
		userNames.append(curUser)
		curUser = str(curUser)
		user_write.write(curUser)
		user_write.write("\n")
		size = size+1

	alphabetize  = open('userNames.txt', 'rU')
	userNames = []
	while(alphabetize.readline()):
		userNames.append(alphabetize.readline())

	user_write = open('userNamesMaster.txt', 'w')

	S = set()
	count = 0
	for e in userNames:
		if e in S:
			continue
		S.add(e)
		count = count+1
		user_write.write(e)
	print count 
	'''


