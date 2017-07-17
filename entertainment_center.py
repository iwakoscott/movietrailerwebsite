import fresh_tomatoes

def main():

    # call populate_movies generator and typecast as a list
    movies = list(fresh_tomatoes.populate_movies())

    # sort the list of movies by reversed ratings i.e. those with higher ratings
    # at the front and those with lower ratings at the back and pass into
    # open_movies_page to be rendered into a website.
    fresh_tomatoes.open_movies_page(sorted(movies, reverse=True))

if __name__ == '__main__':
    main()
