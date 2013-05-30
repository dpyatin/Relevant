import csv
import json
import twitter

def getTimeline(api, userid):
    
    timelineObj = api.GetUserTimeline(user_id=userid, count=200, trim_user=1)
    
    outTimeline = []
        
    for status in timelineObj:
        cur_tweet = []
        cur_line = status.AsJsonString()
        
        try:
            cur_json_obj = json.loads(cur_line)
        except ValueError:
            return None
        
        
        
        cur_tweet.append(removeSpecialTokens(cur_json_obj.get('text')).encode('utf-8'))
        cur_tweet.append(cur_json_obj.get('retweet_count'))
        outTimeline.append(cur_tweet)
        #print "wrote another tweet"
            
    return outTimeline

def removeSpecialTokens(cur_line):
    
    cur_tokens = cur_line.split(' ')

    rs_tokens = []

    for tk in cur_tokens:

        if tk == None or len(tk) == 0:
            continue

        if tk == 'RT' or tk[0] == '@':
            continue
        else:
            rs_tokens.append(tk)

    return ' '.join(rs_tokens)

def main():
    # i/o
    curDataPath = 'UIDlist1.txt'
    outputPath = 'timelinecorpus.csv'
    
    # initialize api
    api = twitter.Api(consumer_key='FuFzMcJWJeZMnYnY9RisPw',
                     consumer_secret='fpBFDpd15WwOkwdJDcCvZECSctcMkfaM8qmiVd1a5Q',
                     access_token_key='567581600-aF8Aweppmj9nbSUZJbMVQdkgvyHBEIy7xNCQGg1h',
                     access_token_secret='UGiKLWfaYEbv8yoqNMVVlFdFv0uaEIYWdRlfVoM')
        
    userids = open(curDataPath, 'r')
    timelineOut = open(outputPath, 'a+b')
    timelineWriter = csv.writer(timelineOut,delimiter=',',dialect='excel')
    
    print "done initializing"
    
    # iterate over all UIDs       
    for line in userids:
        
        if line == None:
            continue

        cur_line = line.strip().replace('\\n',' ')
        
        if len(cur_line) == 0:
            continue
        
        uid = int(cur_line)
        
        try: 
            timelineWriter.writerow(getTimeline(api,uid))
        except:
            print uid
            continue
              
        print "wrote another row"        
                
if __name__ == "__main__":
    main() 