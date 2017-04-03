from ariadne_nda import butterfly


def search(experiment, sample, dataset, channel, feature, id=None, x=None, y=None,
           z=None, width=None, height=None, depth=None):
    return butterfly.proxy(
        '/api/entity_feature',
        params=dict(
            experiment=experiment,
            sample=sample,
            dataset=dataset,
            channel=channel,
            feature=feature,
            id=id,
            x=x,
            y=y,
            z=z,
            width=width,
            height=height,
            depth=depth,
        )
    )
