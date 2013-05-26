import solr
from nltk.corpus import wordnet as wn

#checkKeyWords = [('dog','cat'),('',''),(),()]

topicSet = ['food','weather','celebrity','art', 'animals', 'clothes', 'sports','fantasy']

def getKeyWords():
    str = 'jacket'
    return str.lower()

###
# 
###
def getSolrResult():
    # create a connection to a solr server
    s = solr.SolrConnection('http://127.0.0.1:8983/solr')

    curKeyWord = getKeyWords()
    # do a search
    response = s.query('topics:' + curKeyWord)
    for hit in response.results:
        print hit

###
# give keyword and topic, find the first meaning for both words, and calculate the score, then return scores
# @param: keyword1
# @param: topic
# TODO: try different other similarity score
###
def getSimilarTopic(keyWord):
    
    if keyWord == None or len(keyWord.strip()) == 0:
      raise Exception('ERROR','Key word name is None or Empty')

    rsSet = {}

    curMaxTopicScore = -1
    
    for tp in topicSet:
    
        tmpSet = {}
    
        for r_tk in wn.synsets(keyWord):

            for tk in wn.synsets(tp):
    	    
    	        curScore = r_tk.path_similarity(tk)
    	    
    	        if curScore == None:
    	            continue
    	        else:
    	            tmpSet['rs'] = (r_tk,tk,curScore,tp)
    	            break
    
            if len(tmpSet) == 0:
        	    continue
            else:
        	    break

        if len(tmpSet) == 0:
            tmpSet = None
            continue
        else:
        	tmpTuple = tmpSet.get('rs')

        	if tmpTuple[2] > curMaxTopicScore:
        	    curMaxTopicScore = tmpTuple[2]
        	    rsSet['rs'] = tmpTuple

        tmpSet = None

    return rsSet.get('rs')


def main():

    keyWord = getKeyWords()

    #topic = 'fantasy'

    curRSTuple = getSimilarTopic(keyWord)

    if curRSTuple == None:
        print 'NO MAPPING FOUND'
    else:
        print keyWord + " : " + str(curRSTuple[0].definition)
        print str(curRSTuple[3]) + " : " + str(curRSTuple[1].definition)
        print "Score is : " + str(curRSTuple[2])

'''
    keyWord2 = 'politics.n.01'

    wd1ST = wn.synset(keyWord1)
    print wd1ST

    wd2ST = wn.synset(keyWord2)
    print wd2ST.definition

    print wd1ST.path_similarity(wd2ST)
'''
#    keyword = wn.synsets('dog')

#    for tk in keyword:
#    	print tk.definition
#    	print '************'

#for tk in wn.synsets(keyWord):
#    print tk
#    print tk.definition
#    print '************'

#dogObj = wn.synset('dog.n.01')

#catObj = wn.synset('cat.n.01')

#print dogObj.path_similarity(catObj)


if __name__ == "__main__":
    main() 
