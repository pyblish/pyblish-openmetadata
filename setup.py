#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This setup script packages pyblish_om"""

from setuptools import setup, find_packages


with open('README.txt') as f:
    readme = f.read()


import os
import imp

version_file = os.path.abspath('pyblish_om/version.py')
version_mod = imp.load_source('version', version_file)
version = version_mod.version


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]


setup(
    name='pyblish_om',
    version=version,
    packages=find_packages(),
    url='https://github.com/abstractfactory/pyblish-om',
    license='LGPL',
    author='Marcus Ottosson',
    author_email='marcus@abstractfactory.io',
    description='om pyblish package',
    long_description=readme,
    zip_safe=False,
    classifiers=classifiers
)
