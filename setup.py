#!/usr/bin/python
from setuptools import setup, find_packages

# Import the module version
from immutable_collection import __version__

# Run the setup
setup(
    name             = 'immutable_collection',
    version          = __version__,
    description      = 'Library for interacting with the Rancher 2 v3 API',
    long_description = open('DESCRIPTION.rst').read(),
    author           = 'David Taylor',
    author_email     = 'djtaylor13@gmail.com',
    url              = 'http://github.com/djtaylor/python-immutable-collection',
    license          = 'GPLv3',
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    packages         = find_packages(),
    keywords         = 'tuple immutable collection dictionary dict',
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Terminals',
    ]
)
