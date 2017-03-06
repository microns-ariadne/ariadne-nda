from ariadne_nda import butterfly


def search(experiment, sample, dataset, channel):
    return butterfly.proxy(
        '/api/channel_metadata',
        params=dict(
            experiment=experiment,
            sample=sample,
            dataset=dataset,
            channel=channel,
        )
    )
