#!/usr/bin/env python

# standard library imports
from os.path import exists

# third party related imports
from setuptools import setup, find_packages

# local library imports
from interactor import __version__


setup(
    name='interactor',
    version=__version__,
    # Your name & email here
    author='Yu Liang',
    author_email='yu.liang@thekono.com',
    # If you had interactor.tests, you would also include that in this list
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    # REQUIRED: Your project's URL
    url='https://github.com/yu-liang-kono/interactor',
    # Put your license here. See LICENSE.txt for more information
    license='',
    # Put a nice one-liner description here
    description=('Interactor provides a common interface for performing '
                 'complex user interactions.'),
    long_description=open('README.md').read() if exists("README.md") else "",
    # Any requirements here, e.g. "Django >= 1.1.1"
    install_requires=[

    ],
)
