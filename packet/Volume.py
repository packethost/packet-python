# -*- coding: utf-8 -*-

from .baseapi import BaseAPI
from .Plan import Plan
from .Facility import Facility


class Volume(BaseAPI):

    def __init__(self, data, auth_token, consumer_token=None):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.size = data['size']
        self.state = data['state']
        self.locked = data['locked']
        self.billing_cycle = data['billing_cycle']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.attachments = data['attachments']

        self.plan = Plan(data['plan'])
        self.facility = Facility(data['facility'])

        super(Volume, self).__init__(auth_token, consumer_token)

    def update(self):
        params = {
            "description": self.description,
            "size": self.size,
            "plan": self.plan,
            "locked": self.locked
        }

        return super(Volume, self).call_api("storage/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return super(Volume, self).call_api("storage/%s" % self.id, type='DELETE')

    def attach(self, device_id):
        params = {'device_id': device_id}
        return super(Volume, self).call_api("storage/%s/attachments" % self.id, type='POST', params=params)

    def detach(self):
        for attachment in self.attachments:
            return super(Volume, self).call_api(attachment['href'], type='DELETE')

    def list_snapshots(self, params={}):
        data = super(Volume, self).call_api('storage/%s/snapshots' % (self.id))
        snapshots = list()
        for jsoned in data['snapshots']:
            snapshot = VolumeSnapshot(jsoned, self, self.auth_token, self.consumer_token)
            snapshots.append(snapshot)
        return snapshots

    def create_snapshot(self):
        return super(Volume, self).call_api("storage/%s/snapshots" % self.id, type='POST')

    def __str__(self):
        return "%s" % self.id


class VolumeSnapshot(BaseAPI):

    def __init__(self, data, volume, auth_token, consumer_token=None):
        self.id = data['id']
        self.status = data['status']
        self.timestamp = data['timestamp']
        self.created_at = data['created_at']

        self.volume = volume

        super(VolumeSnapshot, self).__init__(auth_token, consumer_token)

    def delete(self):
        return super(VolumeSnapshot, self).call_api("/storage/%s/snapshots/%s" % (self.volume.id, self.id), type='DELETE')

    def __str__(self):
        return "%s" % self.id
