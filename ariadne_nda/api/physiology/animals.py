from ariadne_npdb.models import animal


def search():
    a = animal.Animal()
    return a.get_all_ids()
