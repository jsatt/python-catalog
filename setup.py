#!/usr/bin/env python

from setuptools import setup

long_description = open('README.rst').read()

setup_args = dict(
    name='pycatalog',
    version='1.2.0',
    description='Data structure for complexe enumeration.',
    long_description=long_description,
    author='Jeremy Satterfield',
    author_email='jsatt@jsatt.com',
    url='https://github.com/jsatt/python-catalog',
    license="MIT License",
    install_requires=[
        'future'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    py_modules=['catalog'],
)

if __name__ == '__main__':
    setup(**setup_args)
