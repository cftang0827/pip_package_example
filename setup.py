#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    'numpy',
]

setup(
    name='pip_package_example',
    version='0.0.1',
    description="A simple example for writing your own package and setup.py",
    author="cftang0827",
    author_email='cftang0827@gmail.com',
    url='https://github.com/cftang0827/pip_package_example',
    install_requires=[
        "numpy>=1.17.0"
    ],
    packages=[
        'pip_package_example',
    ],
    package_dir={'pip_package_example': 'pip_package_example'},
    package_data={'pip_package_example': ['data/*.json']},
    license="MIT license",
    zip_safe=False,
    keywords='pip_package_example',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
