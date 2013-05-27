import csv
import json
import twitter

def getTimeline(api, userid):
    
    timelineObj = api.GetUserTimeline(user_id=userid, count=200, trim_user=1)
    print api.MaximumHitFrequency()
    
    outTimeline = []
        
    for status in timelineObj:
        cur_tweet = []
        cur_line = status.AsJsonString()
        
        try:
            cur_json_obj = json.loads(cur_line)
        except ValueError:
            return None
        
        cur_tweet.append(cur_json_obj.get('text').encode('utf-8'))
        cur_tweet.append(cur_json_obj.get('retweet_count'))
        outTimeline.append(cur_tweet)
        #print "wrote another tweet"
            
    return outTimeline

def main():
    # i/o
    curDataPath = 'sampleids.txt'
    outputPath = 'timelinecorpus.csv'
    
    # initialize api
    api = twitter.Api(consumer_key='J6N9dwxP2ZuVDVOBRbzO1g',
                      consumer_secret='iSDinlyBTQn4814PPKHsbnSHQJCg24aCzdlgCWwPp3U',
                      access_token_key='109161820-h7f8U3vSUU7J4OUlEK7Ts52X607GX7RU5XZ49KHx',
                      access_token_secret='57IXeuOsX2j2ylKiy3FAgbQcSd2U1DmPNd0efJis')
    
    userids = open(curDataPath, 'r')
    timelineOut = open(outputPath, 'wb')
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
        
        timelineWriter.writerow(getTimeline(api,uid))  
                
if __name__ == "__main__":
    main() 