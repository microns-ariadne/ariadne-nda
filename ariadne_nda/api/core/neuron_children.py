import json
from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, xstart, xstop, ystart,
        ystop, zstart, zstop, id):
    x, y, z, width, height, depth = butterfly.convert_bounding_box(
        resolution, xstart, xstop, ystart, ystop, zstart, zstop)
    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='neuron_children',
            id=id,
            x=x,
            y=y,
            z=z,
            width=width,
            height=height,
            depth=depth,
        )
    )
    return dict(child_synapses=json.loads(ret.data))
