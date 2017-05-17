import connexion

from ariadne_npdb.models import cell


def get(cell_id):
    c = cell.Cell()
    q = { 'id': cell_id }
    res = c.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(cell_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
