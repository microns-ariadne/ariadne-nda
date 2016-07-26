import os
import random
import string


class BaseConf(object):
    MONGO_HOST = os.environ.get('MONGO_HOST') or 'localhost'


class DevelopmentConf(BaseConf):
    DEBUG = True


class TestingConf(BaseConf):
    MONGO_DBNAME = ''.join(random.choice(string.ascii_lowercase)
                           for _ in range(16))


config = {
    'development': DevelopmentConf,
    'testing': TestingConf,

    'default': DevelopmentConf
}
