import connexion

from ariadne_npdb.models import cell_collection


def search():
    cc = cell_collection.CellCollection()
    return cc.get_all_ids()
