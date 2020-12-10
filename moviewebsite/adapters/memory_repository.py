import csv
import os
from random import random
from typing import List

from werkzeug.security import generate_password_hash

from moviewebsite.adapters.base_repository import AbstractRepository, RepositoryException
from moviewebsite.domainmodel.actor import Actor
from moviewebsite.domainmodel.director import Director
from moviewebsite.domainmodel.genre import Genre
from moviewebsite.domainmodel.movie import Movie
from moviewebsite.domainmodel.review import Review, make_review
from moviewebsite.domainmodel.user import User
from moviewebsite.domainmodel.watchlist import Watchlist

from moviewebsite.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__movies: List[Movie] = list()
        self.__reviews: List[Review] = list()
        self.__users: List[User] = list()
        self.__genres: List[Genre] = list()

    def add_movie(self, movie: Movie):
        self.__movies.append(movie)

    def get_movies(self) -> List[Movie]:
        return self.__movies

    def get_movies_by_title(self, title: str) -> List[Movie]:
        movies_to_return = list()
        for movie in self.__movies:
            if title in movie.title:
                movies_to_return.append(movie)
        return movies_to_return

    def get_movie_by_index(self, index: int) -> Movie:
        return self.__movies[index]

    def get_movies_by_title_and_year(self, title: str, year: int) -> Movie:
        return next((movie for movie in self.__movies if title.lower() in movie.title.lower()
                     and movie.year == year), None)

    def get_movie_index(self, movie: Movie) -> int:
        return self.__movies.index(movie)

    def get_number_of_movies(self) -> int:
        return len(self.__movies)

    def get_random_movies(self, quantity: int) -> List[Movie]:
        movies_count = self.get_number_of_movies()

        if quantity >= movies_count:
            raise IndexError

        random_index = random.sample(range(1, movies_count), quantity)
        movies = list()
        for index in random_index:
            movies.append(self.get_movie_by_index(index))
        return movies

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, username: str) -> User:
        return next((user for user in self.__users if user.username == username.lower()), None)

    def get_users(self) -> List[User]:
        return self.__users

    def get_number_of_users(self) -> int:
        return len(self.__users)

    def add_review(self, review: Review):
        super().add_review(review)
        self.__reviews.append(review)

    def get_reviews(self) -> List[Review]:
        return self.__reviews

    def get_number_of_reviews(self) -> int:
        return len(self.__reviews)

    def get_genres(self) -> List[Genre]:
        return self.__genres

    def get_genre_by_name(self, name: str) -> Genre:
        return next((genre for genre in self.__genres if genre.genre_name.lower() == name.lower()), None)

    def get_number_of_genres(self) -> int:
        return len(self.__genres)

    def get_movie_actors(self, movie: Movie) -> List[Actor]:
        return movie.actors

    def get_movie_director(self, movie: Movie) -> Director:
        return movie.director

    def get_movie_genres(self, movie: Movie) -> List[Genre]:
        return movie.genres

    def get_user_watchlist(self, user) -> Watchlist:
        return user.watchlist


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_movies(data_path: str, repo: MemoryRepository):
    reader = MovieFileCSVReader(os.path.join(data_path, 'Data1000Movies.csv'))
    reader.read_csv_file()
    for movie in reader.dataset_of_movies:
        repo.add_movie(movie)


def load_users(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(data_row[1], generate_password_hash(data_row[2]))
        repo.add_user(user)


def load_review(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'reviews.csv')):
        review = make_review(data_row[4], int(data_row[3]), repo.get_users()[int(data_row[1])],
                             repo.get_movies()[int(data_row[2])])
        repo.add_review(review)


def populate(data_path: str, repo: MemoryRepository):
    load_movies(data_path, repo)
    load_users(data_path, repo)
    load_review(data_path, repo)


