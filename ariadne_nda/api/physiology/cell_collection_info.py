import connexion

from ariadne_npdb.models import cell_collection


def get(cell_collection_id):
    cc = cell_collection.CellCollection()
    res = cc.find_one(dict(id=cell_collection_id))
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(cell_collection_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
