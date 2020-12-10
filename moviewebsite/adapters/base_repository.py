import abc
from typing import List

from moviewebsite.domainmodel.actor import Actor
from moviewebsite.domainmodel.director import Director
from moviewebsite.domainmodel.genre import Genre
from moviewebsite.domainmodel.movie import Movie
from moviewebsite.domainmodel.review import Review
from moviewebsite.domainmodel.user import User
from moviewebsite.domainmodel.watchlist import Watchlist

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    # THIS IS THE REGION FOR MOVIES
    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds a movie to the list of movies """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies(self) -> List[Movie]:
        """ Returns all movies """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, title: str) -> List[Movie]:
        """ Gets movies by a name """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_index(self, index: int) -> Movie:
        """ Gets a movie using an index """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title_and_year(self, title: str, year: int) -> List[Movie]:
        """ Gets movies using a title and year """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_index(self, movie: Movie) -> int:
        """ Gets the index of the movie """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self) -> int:
        """ Gets the number of movies currently in the database """
        raise NotImplementedError

    @abc.abstractmethod
    def get_random_movies(self, quantity: int) -> List[Movie]:
        """ Gets a random amount of movies based on the quantity specified """
        raise NotImplementedError

    # THIS IS THE REGION FOR USERS
    @abc.abstractmethod
    def add_user(self, user: User):
        """ Adds a user to the database """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str) -> User:
        """ Get a user with a specific username """
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self) -> List[User]:
        """ Gets all users """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_users(self) -> int:
        """ Get the number of users in the repository """
        raise NotImplementedError

    # THIS IS THE REGION FOR REVIEWS
    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a review to the repository.
         If the comment does not have bidirectional links with a User and a Movie, this method raises a
         RepositoryException and does not update the repository.
         """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Comment not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Comment not correctly attached to an Article')

    @abc.abstractmethod
    def get_reviews(self) -> List[Review]:
        """ Gets all the reviews """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_reviews(self) -> int:
        """ Gets the number of genres in the repository """
        raise NotImplementedError

    # THIS IS THE REGION FOR GENRES
    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """ Gets all genres in the repository """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre_by_name(self, name: str) -> Genre:
        """ Gets a specified genre by the genre name """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_genres(self) -> int:
        """ Gets the number of genres in the repository """
        raise NotImplementedError

    # THIS IS THE REGION FOR OTHER GET REQUESTS TO THE DATABASE / REPOSITORY
    @abc.abstractmethod
    def get_movie_actors(self, movie: Movie) -> List[Actor]:
        """ Gets all the actors of a specified movie """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_director(self, movie: Movie) -> Director:
        """ Get a specified movie's director """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_genres(self, movie: Movie) -> List[Genre]:
        """ Get all the genres of a specified movie """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_watchlist(self, user) -> Watchlist:
        """ Returns the watchlist of a specified user """
        raise NotImplementedError
