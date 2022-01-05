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


class BaseAPITest(unittest.TestCase):
    def setUp(self):
        self.auth_token = "fake_auth_token"
        self.consumer_token = "fake_consumer_token"
        self.end_point = "api.packet.net"
        self._user_agent_prefix = "fake_user_agent"

    def test_init_all(self):
        base = packet.baseapi.BaseAPI(
            self.auth_token, self.consumer_token, self._user_agent_prefix
        )
        self.assertEqual(base.end_point, self.end_point)
        self.assertEqual(base.auth_token, self.auth_token)
        self.assertEqual(base.consumer_token, self.consumer_token)
        self.assertEqual(base._user_agent_prefix, self._user_agent_prefix)

    def test_call_api_with_end_point(self):
        base = packet.baseapi.BaseAPI(
            self.auth_token, self.consumer_token, self._user_agent_prefix
        )

        if int(sys.version[0]) == 3:
            self.assertRaisesRegex(
                packet.Error,
                "method type not recognized as one of",
                base.call_api,
                "fake_path",
                "bad_method",
            )


class ResponseErrorTest(unittest.TestCase):
    def setUp(self):
        self.resp500 = obj({"status_code": 500})
        self.errBoom = {"error": "boom"}
        self.errBangBoom = {"errors": ["bang", "boom"]}
        self.exception = Exception("x")

    def test_init_empty(self):
        error = packet.ResponseError(self.resp500, None, None)
        self.assertIn("empty", str(error))

    def test_init_string(self):
        error = packet.ResponseError(self.resp500, "whoops", None)
        self.assertIn("whoops", str(error))

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
