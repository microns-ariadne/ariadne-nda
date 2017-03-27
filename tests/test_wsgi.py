from ariadne_nda import wsgi


def test_wsgi():
    assert hasattr(wsgi, 'app')
