#!/usr/bin/env python
import json

j = 0
with open('movies.json', 'r') as movie:
	with open('keywords.json', 'r') as keyword:
		with open('reviews.json', 'r') as review:
			with open('fulldata.csv','a') as fulldata:
				fulldata.write("adult,backdrop_path,belongs_to_collection,budget,first_genre,other_genres,homepage,id,imdb_id,original_language,overview,popularity,poster_path,company,country,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote,count,reviews,keywords"+"\n")
				for j in range(6455):
					print j
					keywordReadLine = keyword.readline()
					reviewReadLine = review.readline()
					movieReadLine = movie.readline()
					if j == 0:
						keywordReadLine = keywordReadLine[3:]
						reviewReadLine = reviewReadLine[3:]
						movieReadLine = movieReadLine[3:]
					jsonKeyword = json.loads(keywordReadLine)
					jsonReview = json.loads(reviewReadLine)
					jsonMovie = json.loads(movieReadLine)
					fulldata.write(str(jsonMovie['adult'])+",")
					fulldata.write(str(jsonMovie['backdrop_path'])+",")
					if jsonMovie['belongs_to_collection'] is not None:
						fulldata.write("'"+str(jsonMovie['belongs_to_collection']['name'].encode("utf-8"))+","+"'")
					else:
						fulldata.write(",")
					fulldata.write(str(jsonMovie['budget'])+",")
					if len(jsonMovie['genres']) >= 1:
						fulldata.write(str(jsonMovie['genres'][0]['name'])+",")
					else:
						fulldata.write(",")
					i = 0
					fulldata.write("'")
					for i in range(len(jsonMovie['genres'])-1):
						fulldata.write(str(jsonMovie['genres'][i+1]['name'])+" ")
					fulldata.write("'")
					fulldata.write(",")
					fulldata.write(str(jsonMovie['homepage'])+",")
					fulldata.write(str(jsonMovie['id'])+",")
					fulldata.write(str(jsonMovie['imdb_id'])+",")
					fulldata.write(str(jsonMovie['original_language'])+",")
					fulldata.write("'")
					fulldata.write((str(jsonMovie['overview'].encode("utf-8"))+"'"+",").replace("\n"," ").replace("\r"," "))
					fulldata.write(str(jsonMovie['popularity'])+",")
					fulldata.write(str(jsonMovie['poster_path'])+",")
					if len(jsonMovie['production_companies']) >= 1:
						fulldata.write("'"+str(jsonMovie['production_companies'][0]['name'].encode("utf-8"))+"'"+",")
					else:
						fulldata.write(",")
					if len(jsonMovie['production_countries']) >= 1:
						fulldata.write("'")
						fulldata.write(str(jsonMovie['production_countries'][0]['name'].encode("utf-8"))+"',")
					else:
						fulldata.write(",")
					fulldata.write(str(jsonMovie['release_date'])+",")
					fulldata.write(str(jsonMovie['revenue'])+",")
					fulldata.write(str(jsonMovie['runtime'])+",")
					if len(jsonMovie['spoken_languages']) >= 1:
						fulldata.write(str(jsonMovie['spoken_languages'][0]['iso_639_1'])+",")
					else:
						fulldata.write(",")
					fulldata.write(str(jsonMovie['status'])+",")
					fulldata.write("'")
					fulldata.write(str(jsonMovie['tagline'].encode("utf-8"))+"',")
					fulldata.write("'")
					fulldata.write(str(jsonMovie['title'].encode("utf-8"))+"',")
					fulldata.write(str(jsonMovie['video'])+",")
					fulldata.write(str(jsonMovie['vote_average'])+",")
					fulldata.write(str(jsonMovie['vote_count'])+",")
					i = 0
					for i in range(len(jsonReview['results'])):
						if i == 0:
							fulldata.write("'")
						fulldata.write((str(jsonReview['results'][i]['content'].encode("utf-8"))+" ").replace("\n"," ").replace("\r"," "))
						if i == (len(jsonReview['results']) -1):
							fulldata.write("'")
					fulldata.write(",")
					i = 0
					for i in range(len(jsonKeyword['keywords'])):
						if i == 0:
							fulldata.write("'")
						fulldata.write(str(jsonKeyword['keywords'][i]['name'].encode("utf-8"))+" ")
						if i == (len(jsonKeyword['keywords']) -1):
							fulldata.write("'")	
					fulldata.write("\n")