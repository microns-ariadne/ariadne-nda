import connexion

from ariadne_npdb.models import per_cell_metric


def get(cell_metric_id):
    pcmi = per_cell_metric.PerCellMetricInfo()
    q = {'id': cell_metric_id}
    res = pcmi.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(cell_metric_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
