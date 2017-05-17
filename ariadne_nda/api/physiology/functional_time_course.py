import connexion

from ariadne_npdb.models import functional_time_course


def get(run_id, cell_id, channel_id=None, trial_id=None):
    ftc = functional_time_course.FunctionalTimeCourse()
    q = {'run_id': run_id, 'cell_id': cell_id}
    if trial_id:
        q['trial_id'] = trial_id
    res = ftc.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'time course data not found',
            __name__.split('.')[-1]
        )
    if res:
        del res['_id']
    return res
