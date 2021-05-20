#!/usr/bin/env python
# SPDX-License-Identifier: LGPL-3.0-only
import codecs
import os.path

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup


with open("README.md") as readme, open("CHANGELOG.md") as changelog:
    long_description = readme.read() + "\n" + changelog.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="packet-python",
    version=get_version("packet/__init__.py"),
    description="Equinix Metal (Packet) API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/packethost/packet-python",
    author="Equinix Metal Developers",
    author_email="support@equinixmetal.com",
    license="LGPL v3",
    keywords="equinix metal packet api client infrastructure",
    packages=["packet"],
    install_requires="requests",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "requests-mock"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
