#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-splitio',
    version='0.1.0',
    author='Mikayel Aleksanyan',
    author_email='miko@cyberprogrammers.net',
    license='MIT',
    url='https://github.com/mikoblog/pytest-splitio',
    description='Split.io SDK integration for e2e tests',
    long_description=read('README.rst'),
    packages=find_packages(exclude=("tests*",)),
    python_requires='>=3.6',
    install_requires=['pytest>=5.0,<7', 'splitio_client>=8.2,<9'],
    classifiers=[
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'splitio = pytestsplitio.pytest_splitio',
        ],
    },
)
