import json
from ariadne_nda import butterfly


def get(collection, experiment, channel, id):
    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='synapse_parent',
            id=id,
        )
    )
    bfly_json = json.loads(ret.data)
    parents = {}
    for parent in bfly_json:
        if parent.endswith('_pre'):
            parents[bfly_json[parent]] = 1
        if parent.endswith('_post'):
            parents[bfly_json[parent]] = 2
    return dict(parent_neurons=parents)
