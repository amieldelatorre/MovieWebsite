from moviewebsite.domainmodel.movie import Movie
from moviewebsite.domainmodel.watchlist import Watchlist
from typing import List


class User:
    def __init__(self, username: str, password: str):
        self.__username: str = username.strip().lower()
        self.__password: str = password
        self.__watched_movies: List[Movie] = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes: int = 0
        self.__watchlist: Watchlist = Watchlist()

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> List[Movie]:
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @property
    def watchlist(self) -> Watchlist:
        return self.__watchlist

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    def add_to_watchlist(self, movie: Movie):
        self.__watchlist.add_movie(movie)

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if self.__username == other.user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__username < other.user_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__username)
