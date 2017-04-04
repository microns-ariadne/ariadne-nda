import json
from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, xstart, xstop, ystart,
        ystop, zstart, zstop):

    # Scale all by the resolution
    scale = 2 ** resolution

    # Integer division for <x> and <y> origin
    bfly_y = ystart // scale
    bfly_x = xstart // scale
    bfly_z = zstart

    depth = zstop - zstart

    # Integer division of differences for <width> and <height>
    bfly_height = (ystop - ystart) // scale
    bfly_width = (xstop - xstart) // scale

    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='neuron_ids',
            x=bfly_x,
            y=bfly_y,
            z=bfly_z,
            width=bfly_width,
            height=bfly_height,
            depth=depth,
        )
    )
    return dict(ids=json.loads(ret.data))
