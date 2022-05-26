from typing import Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


""" Globally accessible libraries """
db = SQLAlchemy()


def init_app(config_file_path: str = "settings.py", **config: Any) -> Flask:
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_file_path)
    app.config.update(**config)

    """ Initialize Plugins """
    db.init_app(app)
    CORS(app)

    """ Flask context """
    with app.app_context():
        # Include our Routes
        from .ubicacion import routes as ubicacion_routes

        # Register Blueprints
        app.register_blueprint(ubicacion_routes.ubicacion_bp)

        return app
