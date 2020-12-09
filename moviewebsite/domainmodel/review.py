from datetime import datetime
from moviewebsite.domainmodel.user import User
from moviewebsite.domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie: Movie = movie
        self.__review_text: str = review_text.strip()
        self.__user: User = None

        if rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating: int = rating

        now = datetime.now()
        self.__timestamp = datetime.timestamp(now)

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def user(self) -> User:
        return self.__user

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self):
        return datetime.fromtimestamp(self.__timestamp).ctime()

    @user.setter
    def user(self, user: User):
        self.__user = user

    def __repr__(self):
        return f"<Movie {self.__movie.title}, {self.__timestamp}>"

    def __eq__(self, other):
        if self.__movie == other.movie and self.__review_text == other.review_text and self.__rating == other.rating and self.__timestamp == other.timestamp:
            return True
        else:
            return False


def make_review(review_text: str, rating: int, user: User, movie: Movie):
    review = Review(movie, review_text, rating)
    review.user = user
    user.add_review(review)
    movie.add_review(review)
    # print('here')
    return review
