from ariadne_nda import butterfly


def search(experiment):
    return butterfly.proxy(
        '/api/samples',
        params=dict(experiment=experiment),
    )
