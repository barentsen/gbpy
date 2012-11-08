#!/usr/bin/env python

import sys
import os
from setuptools import setup

_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "gbpy"))
import meteorpy
del sys.path[0]

setup(name='gbpy',
    version='1.0',
    description="Collection of Python functions used by Geert, which didn't fit elsewhere.",
    author='Geert Barentsen',
    author_email='geert@barentsen.be',
    license='Copyright the authors.'
)
