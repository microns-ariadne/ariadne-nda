from ariadne_npdb.models import trial


def get(run_id):
    s = trial.Trial()
    q = {'run': run_id}
    res = [i['id'] for i in s.find(q)]
    return res
