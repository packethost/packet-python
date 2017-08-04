# -*- coding: utf-8 -*-

from .Plan import Plan
from .Facility import Facility


class Volume():

    def __init__(self, data, manager):
        self.manager = manager

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
        try:
            self.attached_to = data['attachments'][0]['device']['id']
        except (KeyError, IndexError):
            self.attached_to = None

    def update(self):
        params = {
            "description": self.description,
            "size": self.size,
            "plan": self.plan,
            "locked": self.locked
        }

        return self.manager.call_api("storage/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return self.manager.call_api("storage/%s" % self.id, type='DELETE')

    def attach(self, device_id):
        params = {'device_id': device_id}
        return self.manager.call_api("storage/%s/attachments" % self.id, type='POST', params=params)

    def detach(self):
        for attachment in self.attachments:
            return self.manager.call_api(attachment['href'], type='DELETE')

    def list_snapshots(self, params={}):
        data = self.manager.call_api('storage/%s/snapshots' % (self.id))
        snapshots = list()
        for jsoned in data['snapshots']:
            snapshot = VolumeSnapshot(jsoned, self)
            snapshots.append(snapshot)
        return snapshots

    def create_snapshot(self):
        return self.manager.call_api("storage/%s/snapshots" % self.id, type='POST')

    def create_clone(self):
        return self.manager.call_api("storage/%s/clone" % self.id, type="POST")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)


class VolumeSnapshot():

    def __init__(self, data, volume):
        self.volume = volume

        self.id = data['id']
        self.status = data['status']
        self.timestamp = data['timestamp']
        self.created_at = data['created_at']

    def delete(self):
        return self.volume.manager.call_api("/storage/%s/snapshots/%s" % (self.volume.id, self.id), type='DELETE')

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
