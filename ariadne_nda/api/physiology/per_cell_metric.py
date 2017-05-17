import connexion

from ariadne_npdb.models import per_cell_metric


def get(trial_id, cell_id, cell_metric_id):
    pcm = per_cell_metric.PerCellMetric()
    q = {
        'trial_id': trial_id,
        'cell_id': cell_id,
        'metric_info_id': cell_metric_id,
    }
    res = pcm.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'metric not found',
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
