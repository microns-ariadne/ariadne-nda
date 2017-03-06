from ariadne_nda import butterfly


def search(experiment, sample, dataset, x, y, z, width, height, channel):
    return butterfly.proxy(
        '/api/data',
        params=dict(
            experiment=experiment,
            sample=sample,
            dataset=dataset,
            x=x,
            y=y,
            z=z,
            width=width,
            height=height,
            channel=channel,
        )
    )
