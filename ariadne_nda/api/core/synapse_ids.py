from ariadne_nda import butterfly


def get(collection, experiment, channel, id, resolution, xstart, xstop, ystart,
        ystop, zstart, zstop):

    # Scale all by the resolution
    scale = 2 ** resolution

    # Integer division for <x> and <y> origin
    bfly_y = ystart // scale
    bfly_x = xstart // scale
    bfly_z = zstart // scale

    # Integer division of differences for <width> and <height>
    bfly_height = ( ystop - ystart ) // scale
    bfly_width = ( xstop - xstart ) // scale

    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='synapse_ids',
            id=id,
            x=bfly_x,
            y=bfly_y,
            z=bfly_z,
            width=bfly_width,
            height=bfly_height,
            depth=100,
        )
    )
    return dict(ids=ret.data)
