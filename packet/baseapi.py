# -*- coding: utf-8 -*-
import json
import logging
import requests


class Error(Exception):
    """Base exception class for this module"""
    pass


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

    def call_api(self, method, type='GET', params=None):
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

        if type == 'GET':
            resp = requests.get(url, headers=headers)
        elif type == 'POST':
            print url
            resp = requests.post(url, headers=headers, data=json.dumps(params))
        elif type == 'DELETE':
            resp = requests.delete(url, headers=headers)
        elif type == 'PATCH':
            resp = requests.patch(url, headers=headers, data=json.dumps(params))
        else:
            raise Error(
                'method type not recognizes as one of GET, POST, DELETE or PATCH: %s' % type
            )

        if not resp.content:
            data = None
        elif resp.headers['content-type'].startswith("application/json"):
            try:
                data = resp.json()
            except ValueError as e:
                raise JSONReadError(
                    'Read failed: %s' % e.message
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

        return data
