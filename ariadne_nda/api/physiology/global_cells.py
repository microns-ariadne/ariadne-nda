import connexion

from ariadne_npdb.models import global_cell


def get(animal_id):
    gc = global_cell.GlobalCell()
    q = {'animal_id': animal_id}
    res = [i['id'] for i in gc.find(q)]
    if not res:
        return connexion.problem(
            404,
            'not found',
            'no global cells found for {}'.format(animal_id),
            __name__.split('.')[-1]
        )
    return res
