from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, id):
    ret = butterfly.proxy(
        '/api/entity_feature',
        json=True,
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='synapse_keypoint',
            id=id,
        )
    )
    return dict(keypoint=[ret['x'], ret['y'], ret['z']])
