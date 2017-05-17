import connexion

from ariadne_npdb.models import session


def get(session_id):
    s = session.Session()
    q = {'id': session_id}
    res = s.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'session id {} not found'.format(session_id),
            __name__.split('.')[-1]
        )
    res['animal'] = res['animal']['id']
    del res['_id']
    del res['runs']
    return res
