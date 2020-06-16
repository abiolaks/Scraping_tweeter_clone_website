# Parsing Json Data

import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print(i['tweet']) # checking the tweet 
