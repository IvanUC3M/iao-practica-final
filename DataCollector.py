#!/usr/bin/env python
import requests
import json
URL = "https://api.themoviedb.org/3/authentication/token/new?api_key=690e7bd75cb506aa7ddb08f1d04e6e38"
request = requests.get(URL)
URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=690e7bd75cb506aa7ddb08f1d04e6e38&page=319"
request = requests.get(URL)
data = request.json() 
movieObject = json.loads(request.text)
totalNumberOfPages = movieObject["total_pages"]
for _ in range(totalNumberOfPages):
	