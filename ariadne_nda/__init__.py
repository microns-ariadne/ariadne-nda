from flask import Flask
from ariadne_nda.config import config


def create_app(config_level='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_level])

    from ariadne_nda.api_endpoints import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v0.1')

    return app
