import connexion
from connexion import resolver

from flask import Flask

from ariadne_nda.config import config


def create_app(config_level='default'):
    capp = connexion.App(__name__)

    capp.app.config.from_object(config[config_level])

    capp.add_api(
        'api/anatomy.yaml',
        base_path='/api/v0.1/anatomy',
        resolver=resolver.RestyResolver('ariadne_nda.api.anatomy')
    )

    capp.add_api(
        'api/physiology.yaml',
        base_path='/api/v0.1/physiology',
        resolver=resolver.RestyResolver('ariadne_nda.api.physiology')
    )

    return capp.app
