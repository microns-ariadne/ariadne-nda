import connexion
from connexion import resolver

from ariadne_nda import config


def create_app(config_level='default'):
    capp = connexion.App(__name__)

    capp.app.config.from_object(config.config[config_level])

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

    capp.add_api(
        'api/core.yaml',
        base_path='/api/v0.1',
        resolver=resolver.RestyResolver('ariadne_nda.api.core')
    )

    return capp.app
