from moviewebsite.domainmodel.movie import Movie
from typing import List


class Watchlist:
    def __init__(self):
        self.__movies: List[Movie] = list()

    def add_movie(self, movie: Movie):
        if movie not in self.__movies:
            self.__movies.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__movies:
            self.__movies.remove(movie)

    def get_movie(self, index: int):
        if not self.__movies:
            return None
        elif 0 <= index < len(self.__movies):
            return self.__movies[index]

        else:
            return None

    @property
    def movies(self) -> List[Movie]:
        return self.__movies

    @property
    def size(self) -> int:
        return len(self.__movies)

    @property
    def first_movie_in_watchlist(self) -> Movie:
        if not self.__movies:
            return None
        else:
            return self.__movies[0]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__movies):
            result = self.__movies[self.__index]
            self.__index += 1
            return result
        raise StopIteration
