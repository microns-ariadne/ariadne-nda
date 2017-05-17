import connexion

from ariadne_npdb.models import run


def get(session_id):
    r = run.Run()
    q = { 'session': session_id }
    res = [ i['id'] for i in list(r.find(q))]
    return res or []
