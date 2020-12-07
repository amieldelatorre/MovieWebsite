class Movie:
    def __init__(self, movie_name: str, year: int):
        if movie_name == "" or type(movie_name) is not str:
            self.__title = None
        else:
            self.__title = movie_name.strip()

        if type(year) is not int or year < 1900:
            raise ValueError
        else:
            self.__year = year
