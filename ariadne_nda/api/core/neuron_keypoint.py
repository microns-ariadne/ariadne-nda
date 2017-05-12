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
            feature='neuron_keypoint',
            id=id,
        )
    )

    keypoint = [ret['x'], ret['y'], ret['z']] if ret else []

    return dict(keypoint=keypoint)
