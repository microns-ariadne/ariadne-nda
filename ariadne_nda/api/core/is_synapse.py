from ariadne_nda import butterfly


def get(collection, experiment, channel, id):
    ret = butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='is_synapse',
            id=id,
        )
    )
    return dict(result=butterfly.str2bool(ret.data))
