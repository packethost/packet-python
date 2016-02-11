# -*- coding: utf-8 -*-

from .baseapi import BaseAPI
from .OperatingSystem import OperatingSystem


class Device(BaseAPI):

    def __init__(self, data, auth_token, consumer_token=None):
        self.id = data['id']
        self.plan = data['plan']
        self.hostname = data['hostname']
        self.href = data['href']
        self.userdata = data['userdata']
        self.operating_system = OperatingSystem(data['operating_system'])
        self.locked = data['locked']
        self.tags = data['tags']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.state = data['state']
        self.billing_cycle = data['billing_cycle']
        self.user = data['user']
        self.ip_addresses = data['ip_addresses']

        super(Device, self).__init__(auth_token, consumer_token)

    def update(self):
        params = {
            "hostname": self.hostname,
            "locked": self.locked
        }

        return super(Device, self).call_api("devices/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return super(Device, self).call_api("devices/%s" % self.id, type='DELETE')

    def power_off(self):
        params = { 'type': 'power_off' }
        return super(Device, self).call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def power_on(self):
        params = { 'type': 'power_on' }
        return super(Device, self).call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def reboot(self):
        params = { 'type': 'reboot' }
        return super(Device, self).call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def __str__(self):
        return "%s" % self.hostname
