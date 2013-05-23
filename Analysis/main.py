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

globals.init()
TweetExtraction.makeCorpus()

