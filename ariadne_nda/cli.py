from flask_script import Manager
from ariadne_nda import create_app
from ariadne_nda.logging import config_cli_logging

config_cli_logging()
app = create_app
manager = Manager(app)
manager.add_option('-c', '--config', dest='config_level', default='default',
                   required=False)
manager.set_defaults()
