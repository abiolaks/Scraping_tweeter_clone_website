from bs4 import BeautifulSoup
import requests
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#print(content) # this print the entire raw html page and this is not useful.

# Getting the scrape data into a useful format

# using selectors in BeautifulSoup

#tweet = content.find('p', attrs={"class": "content"}).text
#print(tweet) # This return the content of  the first tweet

# to all tweets use a for loop
# This is what we want to achieve to get the content of all the tweet
#for tweet in content.findAll('p', attrs={"class": "content"}):
   # print(tweet.text.encode('utf-8'))

# Each tweet is in a tweet container, storing this tweet as a dictionary
# looping over the container and storing the data in as an array of dict

tweetArr = [] # creatin an array to store the dict of the data in the containe
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
            "author": tweet.find('h2', attrs={"class": "author"}).text, #.encode('utf-8'),
            "date": tweet.find('h5', attrs={"class": "dateTime"}).text, #.encode('utf-8'),
            "tweet": tweet.find('p', attrs={"class": "content"}).text, #.encode('utf-8'),
            "likes": tweet.find('p', attrs={"class": "likes"}).text, #.encode('utf-8'),
            "shares": tweet.find('p', attrs={"class": "shares"}).text #.encode('utf-8')
            }

    tweetArr.append(tweetObject) # storing the  data dict in an array 
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)


