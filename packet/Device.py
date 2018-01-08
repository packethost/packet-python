# -*- coding: utf-8 -*-

from .OperatingSystem import OperatingSystem


class Device():

    def __init__(self, data, manager):
        self.manager = manager

        self.billing_cycle = data['billing_cycle']
        self.created_at = data['created_at']
        self.facility = data['facility']
        self.hostname = data['hostname']
        self.href = data['href']
        self.id = data['id']
        self.ip_addresses = data['ip_addresses']
        self.locked = data['locked']
        self.operating_system = OperatingSystem(data['operating_system'])
        self.plan = data['plan']
        self.state = data['state']
        self.tags = data['tags']
        self.updated_at = data['updated_at']
        self.user = data['user']

    def update(self):
        params = {
            "hostname": self.hostname,
            "locked": self.locked,
            "tags": self.tags,
        }

        return self.manager.call_api("devices/%s" % self.id, type='PATCH', params=params)

    def delete(self):
        return self.manager.call_api("devices/%s" % self.id, type='DELETE')

    def power_off(self):
        params = {'type': 'power_off'}
        return self.manager.call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def power_on(self):
        params = {'type': 'power_on'}
        return self.manager.call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def reboot(self):
        params = {'type': 'reboot'}
        return self.manager.call_api("devices/%s/actions" % self.id, type='POST', params=params)

    def __str__(self):
        return "%s" % self.hostname

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
