import sys
import logging


class ConsoleHandler(logging.StreamHandler):
    def __init__(self, stream=sys.stdout, error_stream=sys.stderr):
        self.error_stream = error_stream
        super().__init__(stream)


def get_ariadne_nda_logging():
    log = logging.getLogger('ariadne_nda')
    log.addHandler(logging.NullHandler())
    return log


log = get_ariadne_nda_logging()
console = ConsoleHandler()


def config_cli_logging():
    """
    Configure ariadne_nda logging

    By default the ariadne nda logger has no formatters and a Null Handler so
    that others can setup logging as they see fit.  This method is called by
    the cli to toggle console specific handlers
    """
    log.setLevel(logging.DEBUG)
    console.setLevel(logging.INFO)
    log.addHandler(console)
