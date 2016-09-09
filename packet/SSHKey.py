# -*- coding: utf-8 -*-


class SSHKey():

    def __init__(self, data, manager):
        self.manager = manager

        self.id = data['id']
        self.key = data['key']
        self.label = data['label']
        self.fingerprint = data['fingerprint']
        self.href = data['href']
        self.user = data['user']['href']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def update(self):
        params = {
            "label": self.label,
            "key": self.key,
        }

        return self.manager.call_api("ssh-keys/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return self.manager.call_api("ssh-keys/%s" % self.id, type='DELETE')

    def __str__(self):
        return "%s %s" % (self.id, self.label)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
