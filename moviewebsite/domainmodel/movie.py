from moviewebsite.domainmodel.genre import Genre
from moviewebsite.domainmodel.actor import Actor
from moviewebsite.domainmodel.director import Director
from typing import List


class Movie:
    def __init__(self, movie_name: str, year: int):
        if movie_name == "" or type(movie_name) is not str:
            raise ValueError
        else:
            self.__title = movie_name.strip()

        if type(year) is not int or year < 1900:
            raise ValueError
        else:
            self.__year = year

        self.__description: str = ""
        self.__director: Director = Director("")
        self.__actors: List[Actor] = list()
        self.__genres: List[Genre] = list()
        self.__reviews = list()
        self.__runtime_minutes: int = 0
        self.__rating: float = 0
        self.__rating_votes: int = 0
        self.__revenue: float = 0
        self.__metascore: float = 0
        self.__poster_link: str = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def year(self) -> int:
        return self.__year

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> List[Actor]:
        return self.__actors

    @property
    def genres(self) -> List[Genre]:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @property
    def poster_link(self) -> str:
        return self.__poster_link

    @property
    def rating(self) -> float:
        return self.__rating

    @property
    def rating_votes(self) -> int:
        return self.__rating_votes

    @property
    def revenue(self) -> float:
        return self.__revenue

    @property
    def metascore(self) -> int:
        return self.__metascore

    @property
    def reviews(self):
        return self.__reviews

    @title.setter
    def title(self, title: str):
        self.__title = title

    @year.setter
    def year(self, year: int):
        if year >= 1900:
            self.__year = year

    @director.setter
    def director(self, director: Director):
        self.__director = director

    @description.setter
    def description(self, description: str):
        self.__description = description.strip()

    @poster_link.setter
    def poster_link(self, link: str):
        self.__poster_link = link

    @rating.setter
    def rating(self, rate: float):
        self.__rating = rate

    @rating_votes.setter
    def rating_votes(self, votes: int):
        self.__rating_votes = votes

    @revenue.setter
    def revenue(self, rev: float):
        self.__revenue = rev

    @metascore.setter
    def metascore(self, score: int):
        self.__metascore = score

    def add_actor(self, actor: Actor):
        if actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)

    @runtime_minutes.setter
    def runtime_minutes(self, runtime: int):
        if runtime <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if self.__title == other.title and self.year == other.year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__title < other.title:
            return True
        elif self.__title == other.title and self.__year < other.year:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.__title, self.__year))
