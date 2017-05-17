import connexion

from ariadne_npdb.models import trial


def get(trial_id):
    t = trial.Trial()
    q = {'id': trial_id}
    res = t.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'id {} does not exist'.format(trial_id),
            __name__.split('.')[-1]
        )
    del res['_id']
    return res
