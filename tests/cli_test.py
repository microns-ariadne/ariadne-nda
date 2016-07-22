from ariadne_nda import cli


class TestManager(object):

    def test_defaults_present(self):
        assert 'runserver' in cli.manager._commands
        assert 'shell' in cli.manager._commands
