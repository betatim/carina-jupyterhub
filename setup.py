#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Tim Head


# Minimal Python version sanity check (from IPython/Jupyterhub)
from __future__ import print_function

import os
import sys

v = sys.version_info
if v[:2] < (3,3):
    error = "ERROR: Jupyter Hub requires Python version 3.3 or above."
    print(error, file=sys.stderr)
    sys.exit(1)


if os.name in ('nt', 'dos'):
    error = "ERROR: Windows is not supported"
    print(error, file=sys.stderr)


from distutils.core import setup

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))


setup_args = dict(
    name             = 'carinahub',
    packages         = ['carinahub'],
    version          = '0.0.1',
    description      = """Carinahub: Jupyterhub backed by Carina.""",
    long_description = "",
    author           = "Tim Head",
    author_email     = "betatim@gmail.com",
    url              = "http://github.org/betatim/carinahub",
    license          = "BSD",
    platforms        = "Linux, Mac OS X",
    keywords         = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers      = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
