#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import codecs

URL = "https://api.themoviedb.org/3/authentication/token/new?api_key=690e7bd75cb506aa7ddb08f1d04e6e38"
request = requests.get(URL)
URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=690e7bd75cb506aa7ddb08f1d04e6e38&page=1"
request = requests.get(URL)
data = request.json()
movieObject = json.loads(request.text)
totalNumberOfPages = movieObject["total_pages"]
print(totalNumberOfPages)
with codecs.open('data.json', 'a', "utf-8-sig") as outfile:
	for j in range(totalNumberOfPages):
		print("Page "+str(j+1))
		URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=690e7bd75cb506aa7ddb08f1d04e6e38&page="+str(j+1)
		request = requests.get(URL)
		outfile.write(request.text)
		outfile.write("\n")