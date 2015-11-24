#!/usr/bin/env python

import sys
if sys.version_info < (3,):
    print('This package requires Python 3.')
    sys.exit(1)

from distutils.core import setup

import catalog

long_description = open('README').read()

setup_args = dict(
    name='pycatalog',
    version=catalog.__version__,
    description='Data structure for complexe enumeration.',
    long_description=long_description,
    author='Jeremy Satterfield',
    author_email='jsatt@jsatt.com',
    url='https://github.com/jsatt/python-catalog',
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
    ],
    py_modules=['catalog'],
)

if __name__ == '__main__':
    setup(**setup_args)
