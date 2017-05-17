import connexion

from ariadne_npdb.models import animal


def get(animal_id):
    a = animal.Animal()
    res = a.find_one(dict(id=animal_id))
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(animal_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
