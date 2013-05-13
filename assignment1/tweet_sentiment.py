import sys
import json

def load_sent(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    
    return scores

def print_sentiment(sent_file, tweet_file):
    scores = load_sent(sent_file)
    for line in tweet_file:
        raw_tweet = json.loads(line)
        if raw_tweet.has_key('text'):
            tweet_content = raw_tweet['text'].encode('utf-8')
            tweet_score = 0
            for word in tweet_content.split():
                if scores.has_key(word):
                    tweet_score += scores[word]
            print tweet_score
        else:
            print 0
            
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    print_sentiment(sent_file,tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
