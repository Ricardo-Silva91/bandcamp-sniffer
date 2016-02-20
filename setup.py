#!/usr/bin/env python

from setuptools import setup, find_packages
import bandcamp_sniffer
import os

def read(*names):
    values = dict()
    extensions = ['.txt', '.md']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='bandcamp_sniffer',
    version=bandcamp_sniffer.__version__,
    description='automated music downloading via selenium',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords='bandcamp-sniffer bandcamp sniffer for free albums',
    author='Hunter Hammond',
    author_email='huntrar@gmail.com',
    maintainer='Hunter Hammond',
    maintainer_email='huntrar@gmail.com',
    url='https://github.com/huntrar/bandcamp-sniffer',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bandcamp-sniffer = bandcamp_sniffer.bandcamp_sniffer:command_line_runner',
        ]
    },
    install_requires=[
        'lxml',
        'requests'
    ]
)
