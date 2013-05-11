import urllib
import json

proxy = {'http':'http://127.0.0.1:8087'}

def fetchTweets(keyword='microsoft', page=1):
	url = 'http://search.twitter.com/search.json?q=' + keyword + '&page='+str(page)
	response = urllib.urlopen(url, proxies = proxy)
	content = json.load(response)
	tweets = [tweet['text'] for tweet in content['results']]
	return tweets 		

def printTweets():
	for i in range(10):
		tweets = fetchTweets(page = i+1)
		for tweet in tweets:
			encoded_tweet = tweet.encode('utf-8')
			print encoded_tweet

if __name__ == "__main__":
	printTweets()	

