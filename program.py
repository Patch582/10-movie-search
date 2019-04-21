import movie_svc
import requests.exceptions


def print_header():
    print('------------------------------------')
    print('         Movie Search App')
    print('------------------------------------')
    print()


def search_event_loop():

    search = 'ONCE THROUGH LOOP'
    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} movies searching for '{}'".format(len(results), search))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
        except ValueError as ve:
            print('Error: {}'.format(ve))
        except requests.exceptions.ConnectionError as ce:
            print('Error: Your network is down: details: {}'.format(ce))
        except Exception as x:
            print('Unexpected Error: {}'.format(x))

    print('Exiting . . .')


def main():

    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()
