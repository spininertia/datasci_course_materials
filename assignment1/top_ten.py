import sys
import json

def count_hashtags(tweet_file):
    tags_dict = {}
    for line in tweet_file:
        raw_tweet = json.loads(line)
        if raw_tweet.has_key('entities'):
            entities = raw_tweet['entities']
            if entities.has_key('hashtags'):
                hashtags = entities['hashtags']
                for tag in hashtags:
                    tag_name = tag['text'].encode('utf-8')
                    if tags_dict.has_key(tag_name):
                        tags_dict[tag_name] += 1
                    else:
                        tags_dict[tag_name] = 1.0
    
    for tag in sorted(tags_dict, key = tags_dict.get, reverse = True)[:10]:
        print tag, tags_dict[tag]
        
def main():
    tweet_file = open(sys.argv[1])
    count_hashtags(tweet_file)
    
if __name__ == '__main__':
    main()