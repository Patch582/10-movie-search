import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres"
)

def find_movies(search_text):
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    # print(type(movies_list), movies_list)

    # movies = []                       # 1st way of generating list
    # for md in movies_list:
    #    m = MovieResult(
    #         imdb_code=md.get('imdb_code'),
    #         title=md.get('title'),
    #         duration=md.get('duration'),
    #         director=md.get('director'),
    #         year=md.get('year', 0),
    #         rating=md.get('rating', 0),
    #         imdb_score=md.get('imdb_score', 0.0),
    #         keywords=md.get('keywords'),
    #         genre=md.get('genre')
    #     )
    #     movies.append(m)

    # movies = []                       # 2nd way of generating list
    # for md in movies_list:
    #     m = MovieResult(**md)
    #     movies.append(m)

    movies = [                          # 3rd way of generating list
        MovieResult(**md)
        for md in movies_list
    ]

    return movies
