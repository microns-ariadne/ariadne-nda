import urllib

import flask
import requests

from ariadne_nda import config

BUTTERFLY_URL = config.get('BUTTERFLY_URL')


def proxy(url, params=None, json=False):
    url = urllib.parse.urljoin(BUTTERFLY_URL, url)
    r = requests.get(url, params=params)
    if json:
        return r.json()
    else:
        if r.headers.get('Content-Type') == 'image/tif':
            r.headers['Content-Type'] = 'image/tiff'
        return flask.Response(r.content, r.status_code, r.headers.items())


def convert_bounding_box(resolution, xstart, xstop, ystart, ystop, zstart,
                         zstop):
    # Scale all by the resolution
    scale = 2 ** resolution

    # Integer division for <x> and <y> origin
    x = xstart // scale
    y = ystart // scale
    z = zstart

    depth = zstop - zstart

    # Integer division of differences for <width> and <height>
    height = (ystop - ystart) // scale
    width = (xstop - xstart) // scale

    return x, y, z, width, height, depth


def str2bool(val):
    return {b'true': True, b'false': False}.get(val.lower())


def str_encode_ints(array):
    return [str(i) for i in array]
