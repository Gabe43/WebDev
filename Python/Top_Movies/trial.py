from flask import session
import requests

movie_database_api = 'd2d7ce015f741a6d3d29c715b63fd08e'
movie_database_url = 'https://api.themoviedb.org/3/search/movie'
session_id = 'a704a5d8dad9c4e3a52d9d514f32899b4b7a3e2c'
new = 'https://api.themoviedb.org/3/authentication/token/new'


parms = {
    'api_key' : movie_database_api,
    # 'session_id' : session_id,
    'query' : 'Jack Reacher'
}

data = requests.get(url=movie_database_url,params=parms)

movie = data.json()

list = movie.get('results')

print(list)
# # movies = []75780
# id = list[0].get('id')

# movie_details = f'https://api.themoviedb.org/3/movie/{id}'
# det = 'https://api.themoviedb.org/3/movie/75780?api_key=d2d7ce015f741a6d3d29c715b63fd08e&language=en-US'
# parmss = {
#     'api_key' : movie_database_api,
#     # 'session_id' : session_id,
# }

# dat = requests.get(url=movie_details,params=parmss)

# print(dat.json().get('original_title'))
# print(dat.json().get('vote_average'))
# print(dat.json().get('poster_path'))
# for item in range(0,len(list)):
#     movies.append(f"{list[item].get('title')} - {list[item].get('release_date')}")

# print(movies)