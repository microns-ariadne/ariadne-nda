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
    pre = ret['synapse_parent_pre']
    post = ret['synapse_parent_post']

    parents = {}
    if pre == post:
        parents[pre] = 3
    else:
        parents[pre] = 1
        parents[post] = 2

    return dict(parent_neurons=parents)
