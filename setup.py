#!/usr/bin/env python
from setuptools import setup, find_packages


VERSION = 0.1
README = open('README.md').read()


SETUP_REQ = [
    'pytest-runner>=2.8'
]


INSTALL_REQ = [
    'Flask>=0.10.1',
    'Flask-Script>=2.0.5',
    'connexion>=1.1.5',
    'requests>=2.13.0',
    'ariadne-npdb>=0.1',
]


TEST_REQ = [
    'pytest>=2.9.2',
    'pytest-cov>=2.3.0'
]


PACKAGE_DATA = {
    'ariadne_nda.api': ['*.yaml'],
}


setup(
    name='ariadne_nda',
    version=VERSION,
    packages=find_packages(),
    description='Neural Data Access API for the MICrONS ARIADNE project',
    long_description=README,
    setup_requires=SETUP_REQ,
    install_requires=INSTALL_REQ,
    tests_require=TEST_REQ,
    package_data=PACKAGE_DATA,
    include_package_data=True,
    entry_points=dict(console_scripts=['ariadne-nda = ariadne_nda.cli:manager.run']),
    zip_safe=False,
    dependency_links=[
        'git+https://github.com/microns-ariadne/ariadne-npdb.git@40d96a8#egg=ariadne-npdb-0.1',
    ],
)
