from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
import moviewebsite.adapters.base_repository as repo

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    print("Movies: ", repo.repo_instance.get_number_of_movies())
    print("Movies: ", repo.repo_instance.get_number_of_users())
    print("Reviews: ", repo.repo_instance.get_number_of_reviews())
    print("Genres: ", repo.repo_instance.get_number_of_genres())
    return render_template('home.html')
