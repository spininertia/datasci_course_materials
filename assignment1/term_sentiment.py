import sys
import json

def load_sent(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    
    return scores

def term_estimate(sent_file, tweet_file):
    scores = load_sent(sent_file)
    term_scores = {}
    for line in tweet_file:
        raw_tweet = json.loads(line)
        if raw_tweet.has_key('text'):
            tweet = raw_tweet['text'].encode('utf-8')
            new_terms = []
            tweet_score = 0
            for word in tweet.split():
                if scores.has_key(word):
                    tweet_score += scores[word] 
                else:
                    new_terms.append(word)
            for word in new_terms:
                if not term_scores.has_key(word):
                    term_scores[word] = (1,tweet_score)
                else:
                    count,score = term_scores[word]
                    term_scores[word] = (count+1,score + tweet_score)
    
    for term in term_scores.keys():
        count, score = term_scores[term] 
        print term, float(score/count)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    term_estimate(sent_file,tweet_file)
#    lines(sent_file)
#    lines(tweet_file)

if __name__ == '__main__':
    main()
