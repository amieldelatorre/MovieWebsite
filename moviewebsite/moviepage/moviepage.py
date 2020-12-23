from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
import moviewebsite.adapters.base_repository as repo

moviepage_blueprint = Blueprint('moviepage_bp', __name__)


@moviepage_blueprint.route('/Movies', methods=['GET', 'POST'])
def movie_page():
    try:
        title = request.args.get('name')
        year = int(request.args.get('year'))
    except:
        return redirect(url_for('home_bp.home'))

    movie = repo.repo_instance.get_movie_by_title_and_year(title, year)

    return render_template('movie.html',
                           movie=movie)
