import pytest
import json
from ariadne_nda import create_app

from tests.params import experiment_endpoint


class InitApp(object):
    def __init__(self):
        self.app = create_app(config_level='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()

    def cleanup(self):
        self.app_context.pop()


@pytest.fixture(scope='function')
def app(request):
    _app = InitApp()
    request.addfinalizer(_app.cleanup)
    return _app


class BaseEndpoint(object):
    def test_get(self, app, uri, statuscode, resp):
        _resp = app.test_client.get(uri, follow_redirects=True,
                                    content_type='application/json')
        result = json.loads(_resp.data.decode('utf-8'))
        assert result == resp
        assert _resp.status_code == statuscode

    def test_post(self, app, uri, req, statuscode, resp):
        _resp = app.test_client.post(uri, data=json.dumps(req),
                                     follow_redirects=True,
                                     content_type='application/json')
        result = json.loads(_resp.data.decode('utf-8'))
        assert result == resp
        assert _resp.status_code == statuscode


class TestExperiment(BaseEndpoint):
    params = experiment_endpoint.params


def pytest_generate_tests(metafunc):
    func_arg_list = metafunc.cls.params[metafunc.function.__name__]
    arg_names = list(func_arg_list[0])
    metafunc.parametrize(arg_names,
                         [[func_args[name] for name in arg_names]
                          for func_args in func_arg_list])
