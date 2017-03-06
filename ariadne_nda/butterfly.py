import json
import urllib

import requests

from ariadne_nda import config

BUTTERFLY_URL = config.get('BUTTERFLY_URL')


def proxy(url, params=None):
    url = urllib.parse.urljoin(BUTTERFLY_URL, url)
    r = requests.get(url, params=params)
    try:
        content = r.json()
    except json.decoder.JSONDecodeError:
        content = r.content
    return content, r.status_code
