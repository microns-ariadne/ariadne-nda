from ariadne_npdb.models import per_cell_metric


def get(cell_id):
    pcm = per_cell_metric.PerCellMetric()
    q = {'cell_id': cell_id}
    res = pcm.model.distinct('metric_info_id', filter=q)
    return res
