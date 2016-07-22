

class BaseConfig(object):
    pass


class Development(BaseConfig):
    DEBUG = True


config = {
    'development': Development,

    'default': Development
}
