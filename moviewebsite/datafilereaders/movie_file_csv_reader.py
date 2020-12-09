import csv
from moviewebsite.domainmodel.movie import Movie
from moviewebsite.domainmodel.actor import Actor
from moviewebsite.domainmodel.genre import Genre
from moviewebsite.domainmodel.director import Director
from typing import List


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies: List[Movie] = list()
        self.__dataset_of_actors: List[Actor] = list()
        self.__dataset_of_directors: List[Director] = list()
        self.__dataset_of_genres: List[Genre] = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                genres = row['Genre']
                description = row['Description']
                release_year = int(row['Year'])
                director = row["Director"]
                actors = row["Actors"]
                runtime = int(row["Runtime (Minutes)"])
                rating = float(row["Rating"])
                votes = int(row["Votes"])
                try:
                    revenue = float(row["Revenue (Millions)"])
                except ValueError:
                    revenue = row["Revenue (Millions)"]
                try:
                    metascore = int(row["Metascore"])
                except ValueError:
                    metascore = row["Metascore"]

                #print(f"Movie {index} with title: {title}, release year {release_year}")
                #print(index, title, genre, release_year, director, actors, runtime, rating, votes, revenue, metascore)

                movie_director = Director(director)
                movie = Movie(title, release_year)
                movie.director = movie_director
                movie.description = description.strip()
                movie.rating = rating
                movie.rating_votes = votes
                movie.revenue = revenue
                movie.metascore = metascore
                for actor in actors.split(","):
                    actor = Actor(actor)
                    movie.add_actor(actor)
                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)

                movie.runtime_minutes = runtime

                for genre in genres.split(","):
                    genre = Genre(genre)
                    movie.add_genre(genre)
                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre)

                if movie not in self.__dataset_of_movies:
                    self.__dataset_of_movies.append(movie)
                if movie_director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(movie_director)
                index += 1

    @property
    def dataset_of_movies(self) -> List[Movie]:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> List[Actor]:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> List[Director]:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> List[Genre]:
        return self.__dataset_of_genres


"""
reader = MovieFileCSVReader("C:/Users/Amiel/Desktop/projects/uni/CS235FlixSkeleton/datafiles/Data1000Movies.csv")
reader.read_csv_file()
print(f'number of unique movies: {len(reader.dataset_of_movies)}')
print(f'number of unique actors: {len(reader.dataset_of_actors)}')
print(f'number of unique directors: {len(reader.dataset_of_directors)}')
print(f'number of unique genres: {len(reader.dataset_of_genres)}')
#print(f'number of unique genres: {reader.dataset_of_genres}')
"""
