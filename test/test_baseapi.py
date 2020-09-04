# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import sys
import unittest

import packet


class obj(object):
    def __init__(self, dict_):
        self.__dict__.update(dict_)


class ErrorTest(unittest.TestCase):
    def test_cause(self):
        msg = "boom"
        cause = "cause"
        error = packet.Error(msg, cause)
        self.assertIn(error.cause, cause)


class ResponseErrorTest(unittest.TestCase):
    def setUp(self):
        self.resp500 = obj({"status_code": 500})
        self.errBoom = {"error": "boom"}
        self.errBangBoom = {"errors": ["bang", "boom"]}
        self.exception = Exception("x")

    def test_init_empty(self):
        error = packet.ResponseError(self.resp500, None, None)
        self.assertIn("empty", str(error))

    def test_init_error(self):
        error = packet.ResponseError(self.resp500, self.errBoom, self.exception)
        self.assertIn("Error 500: boom", str(error))
        self.assertEqual(500, error.response.status_code)
        self.assertEqual(self.exception, error.cause)

    def test_init_errors(self):
        error = packet.ResponseError(self.resp500, self.errBangBoom, self.exception)
        self.assertIn("Error 500: bang, boom", str(error))
        self.assertEqual(500, error.response.status_code)
        self.assertEqual(self.exception, error.cause)


if __name__ == "__main__":
    sys.exit(unittest.main())
