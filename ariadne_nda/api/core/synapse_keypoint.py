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
    bfly_json = json.loads(ret.data)
    return dict(keypoint=[bfly_json['x'], bfly_json['y'], bfly_json['z']])
