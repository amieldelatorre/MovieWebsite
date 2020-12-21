from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
import moviewebsite.adapters.base_repository as repo

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    number_of_random_movies = 15
    random_movies = repo.repo_instance.get_random_movies(number_of_random_movies)
    for movie in random_movies:
        repo.repo_instance.add_poster_link(movie)
        print(movie.poster_link)

    return render_template('home.html',
                           movies=random_movies
                           )
