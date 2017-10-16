#!/usr/bin/env python

import pypandoc

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

readme = pypandoc.convert_file('README.md', 'rst')
changelog = pypandoc.convert_file('CHANGELOG.md', 'rst')

setup(
    name='packet-python',
    version='1.35',
    description='Packet API client',
    long_description=readme + '\n' + changelog,
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
