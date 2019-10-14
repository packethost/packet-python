#!/usr/bin/env python
# SPDX-License-Identifier: LGPL-3.0-only

# Notes for the not-an-everyday-python-dev for package distribution on pypi
#
# Build the package using `setuptools`:
#
#     python setup.py sdist bdist_wheel
#
# Make sure you have ~/.pypirc correctly populated, as of today should look something like:
#
#     [distutils]
#     index-servers =
#         pypi
#         testpypi
#
#     [pypi]
#     username: username-here
#     password: password-here
#
#     [testpypi]
#     repository: https://test.pypi.org/legacy/
#     username: username-here (not necessarily same as real pypi)
#     password: password-here (not necessarily same as real pypi)
#
# Then upload using twine to testpypi first:
#
#     twine upload -r testpypi dist/*
#
# If all looks good go ahead and tag the repo, push to GH, and then push to real
# pypi:
#
#     twine upload dist/*
#
# Congratulations to me, I've just condensed so many webpages into 30 lines,
# :raised_hands:!

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup

with open("README.md") as readme, open("CHANGELOG.md") as changelog:
    long_description = readme.read() + "\n" + changelog.read()

setup(
    name="packet-python",
    version="1.40.0",
    description="Packet API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/packethost/packet-python",
    author="Packet Developers",
    license="LGPL v3",
    keywords="packet api client",
    packages=["packet"],
    install_requires="requests",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "requests-mock"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
