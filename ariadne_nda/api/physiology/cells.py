from ariadne_npdb.models import cell


def get(run_id):
    c = cell.Cell()
    q = {'run': run_id}
    res = [i['id'] for i in c.find(q, projection=['id'])]
    return res or []
