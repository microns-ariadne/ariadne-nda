from flask import Flask
from flask_pymongo import PyMongo
from ariadne_nda.config import config


mongo = PyMongo()


def create_app(config_level='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_level])

    mongo.init_app(app)

    from ariadne_nda.api_endpoints import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v0.1')

    return app
