import sys
import json

def count_freq(tweet_file):
    freq = {}
    count = 0
    for line in tweet_file:
        raw_tweet = json.loads(line)
        if raw_tweet.has_key('text'):
            tweet = raw_tweet['text'].encode('utf-8')
            for word in tweet.split():
                if freq.has_key(word):
                    freq[word] += 1
                else:
                    freq[word] = 1
                count += 1
    
    for word in freq.keys():
        freq[word] /= count * 1.0
        print word, freq[word]
    
    return freq
    
def main():
    tweet_file = open(sys.argv[1])
    freq = count_freq(tweet_file)
    
if __name__ == '__main__':
    main()