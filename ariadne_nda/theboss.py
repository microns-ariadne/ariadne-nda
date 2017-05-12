import urllib

import flask
import requests
import connexion

from ariadne_nda import config

THEBOSS_URL = config.get('THEBOSS_URL')


def proxy(url, params=None, json=True):
    url = urllib.parse.urljoin(THEBOSS_URL, url)
    r = requests.get(
        url,
        params=params,
        headers={
            'Authorization': connexion.request.headers.get("Authorization"),
        }
    )
    if json:
        return r.json()
    else:
        return flask.Response(r.content, r.status_code, r.headers.items())
