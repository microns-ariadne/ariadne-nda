from ariadne_nda import theboss
from ariadne_nda import butterfly


def get(collection, experiment, channel, resolution, xstart, xstop, ystart,
        ystop, zstart, zstop):

    all_neurons = butterfly.proxy(
        '/api/entity_feature',
        json=True,
        params=dict(
            experiment=collection,
            sample=collection,
            dataset=experiment,
            channel=channel,
            feature='all_neurons',
        )
    )

    all_neurons = butterfly.str_encode_ints(all_neurons)

    boss_ids_url = (
        '/v1/ids/{collection}/{experiment}/{channel}'
        '/{resolution}'
        '/{xstart}:{xstop}'
        '/{ystart}:{ystop}'
        '/{zstart}:{zstop}'
        '/0:1'
    ).format(
        collection=collection,
        experiment=experiment,
        channel=channel,
        resolution=resolution,
        xstart=xstart,
        xstop=xstop,
        ystart=ystart,
        ystop=ystop,
        zstart=zstart,
        zstop=zstop,
    )

    boss_neurons = theboss.proxy(boss_ids_url).get('ids')

    neurons = set(all_neurons) & set(boss_neurons)

    return dict(ids=list(neurons))
