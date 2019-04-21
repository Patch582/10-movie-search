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
    search = input('What movie do you want to search for? ')
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

    # TODO: grab movie data

    resp = requests.get(url)
    resp.raise_for_status()

    # TODO: display movie data

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    # print(type(movies_list), movies_list)

    movies = []
    for md in movies_list:
        m = MovieResult(
            imdb_code=md.get('imdb_code'),
            title=md.get('title'),
            duration=md.get('duration'),
            director=md.get('director'),
            year=md.get('year', 0),
            rating=md.get('rating', 0),
            imdb_score=md.get('imdb_score', 0.0),
            keywords=md.get('keywords'),
            genre=md.get('genre')
        )
        movies.append(m)

    print("Found {} movies searching for '{}'".format(len(movies), search))
    for m in movies:
        print("{} -- {}".format(m.year, m.title))

if __name__ == '__main__':
    main()
