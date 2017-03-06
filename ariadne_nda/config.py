import os


class BaseConfig(object):
    pass


class Development(BaseConfig):
    DEBUG = True


config = {
    'development': Development,
    'default': Development
}


def get(key, level='default'):
    return os.environ.get(key, getattr(config[level], key, None))
