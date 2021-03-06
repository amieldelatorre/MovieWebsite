from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
import moviewebsite.adapters.base_repository as repo

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    number_of_random_movies = 5
    random_movies = repo.repo_instance.get_random_movies(number_of_random_movies)
    for movie in random_movies:
        repo.repo_instance.add_poster_link(movie)

    return render_template('home.html',
                           movies=random_movies
                           )
