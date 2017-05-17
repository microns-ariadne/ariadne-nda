import connexion

from ariadne_npdb.models import run


def get(run_id):
    r = run.Run()
    q = {'id': run_id}
    res = r.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(run_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
