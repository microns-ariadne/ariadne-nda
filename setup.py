#!/usr/bin/env python
from setuptools import setup, find_packages


VERSION = 0.1
README = open('README.md').read()


SETUP_REQ = [
    'pytest-runner>=2.8'
]


INSTALL_REQ = [
    'Flask>=0.10.1',
    'Flask-RESTful>=0.3.5',
    'Flask-Script>=2.0.5',
    'marshmallow>=2.7.3'
]


TEST_REQ = [
    'pytest>=2.9.2',
    'pytest-cov>=2.3.0'
]


setup(
    name='ariadne_nda',
    version=VERSION,
    packages=find_packages(),
    description='Neural Data Access API for the MICrONS ARIADNE project',
    long_description=README,
    setup_requires=SETUP_REQ,
    install_requires=INSTALL_REQ,
    tests_require=TEST_REQ,
    entry_points=dict(console_scripts=['ariadne-nda = ariadne_nda.cli:manager.run']),
    zip_safe=False
)
