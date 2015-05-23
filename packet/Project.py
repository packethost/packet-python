# -*- coding: utf-8 -*-

from .baseapi import BaseAPI


class Project(BaseAPI):

    def __init__(self, data, auth_token, consumer_token=None):
        self.id = data['id']
        self.name = data['name']
        self.payment_method = data['payment_method']
        self.max_projects = data['max_devices']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.devices = data['devices']
        self.invitations = data['invitations']
        self.memberships = data['memberships']
        self.members = data['members']
        self.ssh_keys = data['ssh_keys']

        super(Project, self).__init__(auth_token, consumer_token)

    def update(self):
        params = {
            "name": self.name
        }

        return super(Project, self).call_api("projects/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return super(Project, self).call_api("projects/%s" % self.id, type='DELETE')

    def __str__(self):
        return "%s" % self.name
