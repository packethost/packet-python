#!/bin/bash

set -e
set -x

flake8 --max-line-length=120
cd test && coverage run test_packet.py && coverage report
