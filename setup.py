#!/usr/bin/env python

import os
import pypandoc

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = 'This library provides the python client for the Packet API.'
if os.path.isfile('README.md') and os.path.isfile('CHANGELOG.md'):
    readme = pypandoc.convert_file('README.md', 'rst')
    changelog = pypandoc.convert_file('CHANGELOG.md', 'rst')
    long_description = readme + '\n' + changelog

setup(
    name='packet-python',
    version='1.36.0',
    description='Packet API client',
    long_description=long_description,
    url='https://github.com/packethost/packet-python',
    author='Packet Developers',
    license='LGPL v3',
    keywords='packet api client',
    packages=['packet'],
    install_requires='requests',
    setup_requires='pypandoc',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ])
