from ariadne_npdb.models import session


def get(animal_id):
    s = session.Session()
    q = {'animal.id': animal_id}
    res = [i['id'] for i in list(s.find(q))]
    return res
