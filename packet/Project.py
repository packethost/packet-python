# -*- coding: utf-8 -*-


class Project():

    def __init__(self, data, manager):
        self.manager = manager

        self.id = data['id']
        self.name = data['name']
        self.payment_method = data['payment_method']
        self.max_projects = data.get('max_devices')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.devices = data['devices']
        self.invitations = data['invitations']
        self.memberships = data['memberships']
        self.members = data['members']
        self.ssh_keys = data['ssh_keys']

    def update(self):
        params = {
            "name": self.name
        }

        return self.manager.call_api("projects/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return self.manager.call_api("projects/%s" % self.id, type='DELETE')

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
