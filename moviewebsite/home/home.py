from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
import moviewebsite.adapters.base_repository as repo

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    print(repo.repo_instance.get_movies_by_title_and_year('Guardian', 2014))
    return render_template('home.html')
