"""Initialize Flask"""

import os
from flask import Flask
import moviewebsite.adapters.base_repository as repo
from moviewebsite.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    """Construct the core application"""

    # Creating the Flask object
    app = Flask(__name__)

    # Configure the app from configuration-file settings
    app.config.from_object('config.Config')
    data_path = os.path.abspath("moviewebsite/datafiles")

    if test_config is not None:
        # Load test configuration, and override any configuration settings
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    #  Create the the MemoryRepository implementation for a memory-based repository
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application - these steps require an application context
    with app.app_context():
        # Register blueprints

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .moviepage import moviepage
        app.register_blueprint(moviepage.moviepage_blueprint)

    return app

