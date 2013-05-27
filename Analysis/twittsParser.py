import json

def getEnMessage(cur_line):
    
    try:
        cur_json_obj = json.loads(cur_line)
    except ValueError:
        return None

    user_obj = cur_json_obj.get('user')

    if user_obj == None:
        return None

    if user_obj.get('lang') != 'en':
        return None

    cur_text = cur_json_obj.get('text')

    if cur_text == None:
        return None

    return removeSpecialTokens(cur_text)

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


def getAllMessage(cur_line):

    cur_json_obj = json.loads(cur_line)

    cur_text = cur_json_obj.get('text')

    if cur_text == None:
        return

    print cur_text


def main():
    #curDataPath = '/Users/weiyin/Documents/Publishing_Hackathon/twitts/stage_data/sample.json'
    curDataPath = '/Users/weiyin/Documents/Publishing_Hackathon/twitts/org_data/tweet-stream.json'
    outputDataPath = '/Users/weiyin/Documents/Publishing_Hackathon/twitts/output/twitts_text_output.txt'

    f_open = open(curDataPath)
    f_write = open(outputDataPath,'w')

    for line in f_open:

        if line == None:
            continue

        cur_line = line.strip().replace('\\n',' ')
        
        if len(cur_line) == 0:
            continue

        cur_output = getEnMessage(cur_line)
        if cur_output == None:
            continue
        #print cur_output

        f_write.write(cur_output.encode('utf-8') + '\n')
        #getAllMessage(cur_line)


if __name__ == "__main__":
    main() 
