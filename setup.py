#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = """This library provides the python client for the Packet API."""

if os.path.isfile("README.md"):
    with open('README.md') as file:
        long_description = file.read()

setup(
    name='packet-python',
    version='1.0',
    description='Packet API client',
    author='Aaron Welch ( http://www.packet.net )',
    author_email='welch@packet.net',
    url='https://github.com/packethost/packet-python.git',
    packages=['packet'],
    install_requires=['requests'],
#    test_suite='packet.tests',
    license='LGPL v3',
    keywords='packet api client',
    long_description=long_description
)
