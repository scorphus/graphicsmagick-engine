#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from graphicsmagick_engine import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'colorama',
    'preggy',
    'ipdb',
    'coveralls',
    'numpy',
]

setup(
    name='graphicsmagick_engine',
    version=__version__,
    description='GraphicsMagick imaging engine for thumbor.',
    long_description='''
GraphicsMagick imaging engine for thumbor.
''',
    keywords='thumbor imaging graphicsmagick',
    author='Globo.com',
    author_email='timehome@corp.globo.com',
    url='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'thumbor',
        'pgmagick>=0.5.6',
    ],
    extras_require={
        'tests': tests_require,
    }
)
