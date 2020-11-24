# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import json
import logging
import requests

from packet import __version__


class Error(Exception):  # pragma: no cover
    """Base exception class for this module"""

    def __init__(self, msg, cause=None):
        super(Error, self).__init__(msg)
        self._cause = cause

    @property
    def cause(self):
        """The underlying exception causing the error, if any."""
        return self._cause


class ResponseError(Error):
    def __init__(self, resp, data, exception=None):
        if not data:
            msg = "(empty response)"
        elif "error" in data:
            msg = data["error"]
        elif "errors" in data:
            msg = ", ".join(data["errors"])
        super(ResponseError, self).__init__(
            "Error {0}: {1}".format(resp.status_code, msg), exception
        )
        self._response = resp

    @property
    def response(self):
        """The Requests response which failed"""
        return self._response


class JSONReadError(Error):
    pass


class BaseAPI(object):
    """
        Basic api class for
    """

    def __init__(self, auth_token, consumer_token, user_agent=""):
        self.auth_token = auth_token
        self.consumer_token = consumer_token
        self.end_point = "api.packet.net"
        self._user_agent_prefix = user_agent
        self._log = logging.getLogger(__name__)

    @property
    def user_agent(self):
        return "{}packet-python/{} {}".format(
            self._user_agent_prefix, __version__, requests.utils.default_user_agent()
        ).strip()

    def call_api(self, method, type="GET", params=None):  # noqa
        if params is None:
            params = {}

        url = "https://" + self.end_point + "/" + method

        headers = {
            "X-Auth-Token": self.auth_token,
            "X-Consumer-Token": self.consumer_token,
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }

        # remove token from log
        headers_str = str(headers).replace(self.auth_token.strip(), "TOKEN")
        self._log.debug("%s %s %s %s" % (type, url, params, headers_str))
        try:
            if type == "GET":
                url = url + "%s" % self._parse_params(params)
                resp = requests.get(url, headers=headers)
            elif type == "POST":
                resp = requests.post(
                    url,
                    headers=headers,
                    data=json.dumps(
                        params, default=lambda o: o.__dict__, sort_keys=True, indent=4
                    ),
                )
            elif type == "DELETE":
                resp = requests.delete(url, headers=headers)
            elif type == "PATCH":
                resp = requests.patch(url, headers=headers, data=json.dumps(params))
            else:  # pragma: no cover
                raise Error(
                    "method type not recognized as one of GET, POST, DELETE or PATCH: %s"
                    % type
                )
        except requests.exceptions.RequestException as e:  # pragma: no cover
            raise Error("Communcations error: %s" % str(e), e)

        if not resp.content:
            data = None
        elif resp.headers.get("content-type", "").startswith("application/json"):
            try:
                data = resp.json()
            except ValueError as e:  # pragma: no cover
                raise JSONReadError("Read failed: %s" % e.message, e)
        else:
            data = resp.content  # pragma: no cover

        if not resp.ok:  # pragma: no cover
            raise ResponseError(resp, data)

        try:
            resp.raise_for_status()
        except requests.HTTPError as e:  # pragma: no cover
            raise ResponseError(resp, data, e)

        self.meta = None
        try:
            if data and data["meta"]:
                self.meta = data["meta"]
        except (KeyError, IndexError):
            pass

        return data

    def _parse_params(self, params):
        vals = list()
        for k, v in params.items():
            vals.append(str("%s=%s" % (k, v)))
        return "?" + "&".join(vals)
