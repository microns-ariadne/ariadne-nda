import os


class BaseConfig(object):
    THEBOSS_URL = 'https://api.theboss.io'


class Development(BaseConfig):
    DEBUG = True


config = {
    'development': Development,
    'default': Development
}


def get(key, level='default'):
    return os.environ.get(key, getattr(config[level], key, None))
