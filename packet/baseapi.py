# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import json
import logging
import requests


class Error(Exception):  # pragma: no cover
    """Base exception class for this module"""

    def __init__(self, msg, cause=None):
        super(Error, self).__init__(msg)
        self._cause = cause

    @property
    def cause(self):
        """The underlying exception causing the error, if any."""
        return self._cause


class JSONReadError(Error):
    pass


class BaseAPI(object):
    """
        Basic api class for
    """

    def __init__(self, auth_token, consumer_token):
        self.auth_token = auth_token
        self.consumer_token = consumer_token
        self.end_point = "api.packet.net"
        self._log = logging.getLogger(__name__)

    def call_api(self, method, type="GET", params=None):  # noqa
        if params is None:
            params = {}

        paginated_data = {}
        page = 1

        while True:
            url = "https://" + self.end_point + "/" + method
            if page > 1:
                url = url + f"?page={page}&per_page={params['per_page']}"

            headers = {
                "X-Auth-Token": self.auth_token,
                "X-Consumer-Token": self.consumer_token,
                "Content-Type": "application/json",
            }

            headers_str = str(headers).replace(self.auth_token.strip(), "TOKEN")
            self._log.debug("%s %s %s %s" % (type, url, params, headers_str))
            try:
                if type == "GET":
                    url = url + "%s" % self._parse_params(params)
                    resp = requests.get(url, headers=headers)
                elif type == "POST":
                    resp = requests.post(url, headers=headers, data=json.dumps(params))
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

            if paginated_data == {}:
                paginated_data = data
            elif type == "GET":
                data_keys = list(data.keys())
                # Round about way of getting desired key, but shouldn't be a problem with
                # current api response since it seems like data only contains max two keys
                append_key = data_keys[0] if (data_keys[0] != "meta") else data_keys[1]
                for things in data[append_key]:
                    paginated_data[append_key].append(things)
                paginated_data["meta"] = data["meta"]

            if not resp.ok:  # pragma: no cover
                msg = data
                if not data:
                    msg = "(empty response)"
                elif "errors" in data:
                    msg = ", ".join(data["errors"])
                raise Error("Error {0}: {1}".format(resp.status_code, msg))

            try:
                resp.raise_for_status()
            except requests.HTTPError as e:  # pragma: no cover
                raise Error("Error {0}: {1}".format(resp.status_code, resp.reason), e)

            if (
                type != "GET" or
                not paginated_data.get("meta") or
                paginated_data["meta"]["next"] is None
            ):
                break

            page += 1

        self.meta = None
        try:
            if paginated_data and paginated_data["meta"]:
                self.meta = paginated_data["meta"]
        except (KeyError, IndexError):
            pass

        return paginated_data

    def _parse_params(self, params):
        vals = list()
        for k, v in params.items():
            vals.append(str("%s=%s" % (k, v)))
        return "?" + "&".join(vals)
