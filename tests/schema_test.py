from ariadne_nda import schema


class TestExperimentSchema(object):
    def test_success(self):
        _schema = schema.ExperimentSchema()
        exp_dict, errors = _schema.load({'name': 'ECS_test_9'})
        assert not errors
        assert exp_dict.pop('name') == 'ECS_test_9'
        assert not exp_dict
        exp_dict, errors = _schema.load({'name': 'ECS_test_9',
                                         'description': 'This is a test'})
        assert not errors
        assert exp_dict.pop('name') == 'ECS_test_9'
        assert exp_dict.pop('description') == 'This is a test'
        assert not exp_dict
