from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, xstart, xstop, ystart,
        ystop, zstart, zstop):
    x, y, z, width, height, depth = butterfly.convert_bounding_box(
        resolution, xstart, xstop, ystart, ystop, zstart, zstop)
    ret = butterfly.proxy(
        '/api/entity_feature',
        json=True,
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            resolution=resolution,
            feature='synapse_ids',
            x=x,
            y=y,
            z=z,
            width=width,
            height=height,
            depth=depth,
        )
    )
    return dict(ids=butterfly.str_encode_ints(ret))
