import urllib

import flask
import requests

from ariadne_nda import config

BUTTERFLY_URL = config.get('BUTTERFLY_URL')


def proxy(url, params=None):
    url = urllib.parse.urljoin(BUTTERFLY_URL, url)
    r = requests.get(url, params=params)
    if r.headers.get('Content-Type') == 'image/tif':
        r.headers['Content-Type'] = 'image/tiff'
    return flask.Response(r.content, r.status_code, r.headers.items())
