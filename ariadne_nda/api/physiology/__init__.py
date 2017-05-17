import ariadne_npdb

from ariadne_nda import config

NPDB_HOST = config.get('NPDB_HOST')
NPDB_USERNAME = config.get('NPDB_USERNAME')
NPDB_PASSWORD = config.get('NPDB_PASSWORD')
NPDB_DATABASE = config.get('NPDB_DATABASE')
NPDB_SSL = { 'true': True, 'false': False}.get(
    config.get('NPDB_SSL').lower(), False)
NPDB_PORT = int(config.get('NPDB_PORT'))

AUTH = None
if all([NPDB_USERNAME, NPDB_PASSWORD]):
    AUTH = dict(username=NPDB_USERNAME, password=NPDB_PASSWORD)

ariadne_npdb.connect(
    NPDB_HOST,
    NPDB_DATABASE,
    auth=AUTH,
    port=NPDB_PORT,
    ssl=NPDB_SSL
)
