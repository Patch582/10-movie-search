import requests
import collections


def main():

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
