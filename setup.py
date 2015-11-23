#!/usr/bin/env python

from setuptools import setup

import catalog

long_description = open('README.md').read()

setup_args = dict(
    name='pycatalog',
    version=catalog.__version__,
    description='Data structure for complexe enumeration.',
    long_description=long_description,
    author='Jeremy Satterfield',
    author_email='jsatt@jsatt.com',
    url='https://github.com/jsatt/python-catalog',
    license="MIT License",
    platform='any',
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
