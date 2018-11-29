#!/usr/bin/env python
import json
import codecs
import requests

URL = "https://api.themoviedb.org/3/authentication/token/new?api_key=690e7bd75cb506aa7ddb08f1d04e6e38"
request = requests.get(URL)
with open('Movie_data.json') as infile:
	with codecs.open('reviews.json', 'a', "utf-8-sig") as reviews:
		j = 0
		for line in infile:
			if j == 0:
				line=line[6:]
			j=j+1
			jsonline = json.loads(line)
			jsonline['results'][0]['id']
			i = 0
			print "Page " + str(j)
			for _ in range(len(jsonline['results'])):
				URL="https://api.themoviedb.org/3/movie/"+str(jsonline['results'][i]['id'])+"/reviews?api_key=690e7bd75cb506aa7ddb08f1d04e6e38"
				i=i+1
				request = requests.get(URL)
				reviews.write(request.text)
				reviews.write("\n")