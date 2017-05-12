from ariadne_nda import butterfly


def search(experiment, sample):
    return butterfly.proxy(
        '/api/datasets',
        params=dict(
            experiment=experiment,
            sample=sample,
        )
    )
