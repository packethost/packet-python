# -*- coding: utf-8 -*-
from .baseapi import BaseAPI


class SSHKey(BaseAPI):

    def __init__(self, data, auth_token, consumer_token=None):
        self.id = data['id']
        self.key = data['key']
        self.label = data['label']
        self.fingerprint = data['fingerprint']
        self.href = data['href']
        self.user = data['user']['href']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        super(SSHKey, self).__init__(auth_token, consumer_token)

    def update(self):
        params = {
            "label": self.label,
            "key": self.key,
        }

        return super(SSHKey, self).call_api("ssh-keys/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return super(SSHKey, self).call_api("ssh-keys/%s" % self.id, type='DELETE')

    def __str__(self):
        return "%s %s" % (self.id, self.label)
