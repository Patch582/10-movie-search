import movie_svc


def print_header():
    print('------------------------------------')
    print('         Movie Search App')
    print('------------------------------------')
    print()


def search_event_loop():

    search = 'ONCE THROUGH LOOP'
    while search != 'x':
        search = input('Movie search text (x to exit): ')
        results = movie_svc.find_movies(search)
        print("Found {} movies searching for '{}'".format(len(results), search))
        for r in results:
            print("{} -- {}".format(r.year, r.title))

    print('Exiting . . .')

def main():

    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()
