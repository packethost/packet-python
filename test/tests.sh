#!/bin/bash

set -e
set -x

cd test && coverage run test_packet.py && coverage report
