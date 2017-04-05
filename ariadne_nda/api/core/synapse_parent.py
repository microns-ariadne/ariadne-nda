from ariadne_nda import butterfly


def get(collection, experiment, channel, id):
    ret = butterfly.proxy(
        '/api/entity_feature',
        json=True,
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='synapse_parent',
            id=id,
        )
    )
    parents = {}
    for parent in ret:
        if parent.endswith('_pre'):
            parents[ret[parent]] = 1
        if parent.endswith('_post'):
            parents[ret[parent]] = 2
    return dict(parent_neurons=parents)
