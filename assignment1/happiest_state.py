import sys
import json

scores = {}

def load_sent(sent_file):    
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)

def tweet_sentiment(tweet):
    tweet_score = 0
    if tweet.has_key('text'):
        tweet_content = tweet['text'].encode('utf-8')
        for word in tweet_content.split():
            if scores.has_key(word):
                tweet_score += scores[word]
    return tweet_score

def state_sentiment(tweet_file):
    state_sent = dict()
    for line in tweet_file:
        tweet = json.loads(line)
        tweet_score = tweet_sentiment(tweet)
        if tweet.get('place') != None:
            place = tweet['place']
            if place.get('country') != None and place.get('full_name') != None:
                if place['country'] == 'United States':
                    state = place['full_name'][-2:]
                    if state in state_sent:
                        count, score = state_sent[state]
                        state_sent[state] = (count+1, score + tweet_score)
                    else:
                        state_sent[state] = (1, tweet_score)
    
    state_score = {}
    for key in state_sent.keys():
        state_score[key] = 1.0 * state_sent[key][1] / state_sent[key][0]
    
#    for key in sorted(state_score, key = state_score.get, reverse = True):
#        print key, state_score[key]
        
    print max(state_score, key = state_score.get)
                    
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    load_sent(sent_file)
    state_sentiment(tweet_file)
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()