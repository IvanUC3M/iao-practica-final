#!/usr/bin/env python
import requests
import json


Nombres = ["Venom", "Inventada", "Pokemon"]
URL = "http://www.omdbapi.com/?apikey=f5a1c7cc&t=Venom"
fichero2=open('dataID.json', 'w')

for x in Nombres:
  '''consigue el id por titulo'''
  URL = "http://www.omdbapi.com/?apikey=f5a1c7cc&t="+x
  request = requests.get(URL) 
  data = request.json() 
  print(URL)
  json.dump(data, fichero2)
  idexterno=data["imdbID"]  
  fichero2.write("\n")
  
  '''le pasa le id para tener los comentarios de la otra pagina'''
  URL3= "https://api.themoviedb.org/3/find/"+idexterno+"?api_key=690e7bd75cb506aa7ddb08f1d04e6e38&language=en-US&external_source=imdb_id"
  request = requests.get(URL3)
  data = request.json() 
  fichero=open('data.json', 'w')
  json.dump(data, fichero)
  fichero.write("\n")
  print(data)	
 

  
fichero2.close()
fichero.close()
 
