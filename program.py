import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genre"
)

def print_header():
    print('------------------------------------')
    print('         Movie Search App')
    print('------------------------------------')
    print()


def main():

    print_header()

    # TODO: grab search key & set URL
    search = 'capital'
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

    # TODO: grab movie data

    resp = requests.get(url)
    resp.raise_for_status()

    # TODO: display movie data

    movie_data = resp.json()
    movies = movie_data.get('hits')

    print(type(movies), movies)

if __name__ == '__main__':
    main()
