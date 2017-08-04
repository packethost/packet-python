# -*- coding: utf-8 -*-
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
        self.end_point = 'api.packet.net'
        self._log = logging.getLogger(__name__)

    def call_api(self, method, type='GET', params=None):  # pragma: no cover
        if params is None:
            params = {}

        url = 'https://' + self.end_point + '/' + method

        headers = {'X-Auth-Token': self.auth_token,
                   'X-Consumer-Token': self.consumer_token,
                   'Content-Type': 'application/json'}

        # remove token from log
        headers_str = str(headers).replace(self.auth_token.strip(), 'TOKEN')
        self._log.debug('%s %s %s %s' %
                        (type, url, params, headers_str))
        try:
            if type == 'GET':
                url = url + '%s' % self._parse_params(params)
                resp = requests.get(url, headers=headers)
            elif type == 'POST':
                resp = requests.post(url, headers=headers,
                                     data=json.dumps(params))
            elif type == 'DELETE':
                resp = requests.delete(url, headers=headers)
            elif type == 'PATCH':
                resp = requests.patch(url, headers=headers,
                                      data=json.dumps(params))
            else:
                raise Error(
                    'method type not recognized as one of GET, POST, DELETE or PATCH: %s' % type
                )
        except requests.exceptions.RequestException as e:
            raise Error('Communcations error: %s' % str(e), e)
        if not resp.content:
            data = None
        elif resp.headers.get("content-type", "").startswith("application/json"):
            try:
                data = resp.json()
            except ValueError as e:
                raise JSONReadError(
                    'Read failed: %s' % e.message, e
                )
        else:
            data = resp.content

        if not resp.ok:
            msg = data
            if not data:
                msg = "(empty response)"
            elif 'errors' in data:
                msg = ', '.join(data['errors'])
            raise Error(
                'Error {0}: {1}'.format(resp.status_code, msg)
            )
        try:
            resp.raise_for_status()
        except requests.HTTPError as e:
            raise Error('Error {0}: {1}'.format(resp.status_code,
                                                resp.reason), e)
        self.meta = None
        try:
            if data and data['meta']:
                self.meta = data['meta']
        except (KeyError, IndexError):
            pass
        return data

    def _parse_params(self, params):  # pragma: no cover
        vals = list()
        for k, v in params.items():
            vals.append(str("%s=%s" % (k, v)))
        return "?" + "&".join(vals)
