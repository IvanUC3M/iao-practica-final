#!/usr/bin/env python
import requests
import json
URL = "http://www.omdbapi.com/?apikey=f5a1c7cc&t=Venom"
request = requests.get(URL)
data = request.json() 
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)