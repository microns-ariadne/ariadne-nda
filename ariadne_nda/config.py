import os


class BaseConfig(object):
    THEBOSS_URL = 'https://api.theboss.io'
    BUTTERFLY_URL = None
    NPDB_HOST = None
    NPDB_SSL = 'False'
    NPDB_USERNAME = None
    NPDB_PASSWORD = None
    NPDB_DATABASE = 'npdb'
    NPDB_PORT='27017'


class Development(BaseConfig):
    DEBUG = True


config = {
    'development': Development,
    'default': Development
}


def get(key, level='default'):
    return os.environ.get(key, getattr(config[level], key, None))
