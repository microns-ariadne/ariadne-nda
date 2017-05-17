import connexion

from ariadne_npdb.models import raw_eye_tracking


def get(trial_id):
    ret = raw_eye_tracking.RawEyeTracking()
    q = {'trial_id': trial_id}
    res = ret.find_one(q)
    if not res:
        return connexion.problem(
            404,
            'not found',
            'raw eye tracking data for trial {} not found'.format(trial_id),
            __name__.split('.')[-1]
        )
    if res:
        del res['_id']
    return res
