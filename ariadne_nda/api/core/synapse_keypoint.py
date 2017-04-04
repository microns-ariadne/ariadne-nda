import json
from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, id):
    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='synapse_keypoint',
            id=id,
        )
    )
    return dict(keypoint=list(json.loads(ret.data).values()))
