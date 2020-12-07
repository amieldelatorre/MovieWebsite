import csv
import os

from werkzeug.security import generate_password_hash
from moviewebsite.adapters.base_repository import AbstractRepository, RepositoryException
from moviewebsite.domainmodel.movie import Movie


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__var = None

    def add_movie(self, movie: Movie):
        pass


def populate():
    pass