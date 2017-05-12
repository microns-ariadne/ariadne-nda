from ariadne_nda import butterfly


def search(experiment, sample, dataset):
    return butterfly.proxy(
        '/api/channels',
        params=dict(
            experiment=experiment,
            sample=sample,
            dataset=dataset,
        )
    )
