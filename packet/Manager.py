# -*- coding: utf-8 -*-
from .baseapi import BaseAPI
from .Plan import Plan
from .Device import Device
from .SSHKey import SSHKey
from .Project import Project
from .Facility import Facility
from .OperatingSystem import OperatingSystem
from .Volume import Volume


class Manager(BaseAPI):
    def __init__(self, auth_token, consumer_token=None):
        super(Manager, self).__init__(auth_token, consumer_token)

    def get_user(self):
        return super(Manager, self).call_api("user")

    def list_facilities(self, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api("facilities%s" % pmtrs)
        facilities = list()
        for jsoned in data['facilities']:
            facility = Facility(jsoned)
            facilities.append(facility)
        return facilities

    def list_devices(self, project_id, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('projects/%s/devices%s' % (project_id, pmtrs))
        devices = list()
        for jsoned in data['devices']:
            device = Device(jsoned, self.auth_token, self.consumer_token)
            devices.append(device)
        return devices

    def create_device(self, project_id, hostname, plan, facility,
                      operating_system, billing_cycle="hourly", userdata="",
                      locked=False, features={}):
        params = {
            'hostname': hostname,
            'project_id': project_id,
            'plan': plan,
            'facility': facility,
            'operating_system': operating_system,
            'billing_cycle': billing_cycle,
            'userdata': userdata,
            'locked': locked,
            'features': features,
        }
        data = super(Manager, self).call_api('projects/%s/devices' % project_id, type='POST', params=params)
        return Device(data, self.auth_token, self.consumer_token)

    def get_device(self, device_id):
        data = super(Manager, self).call_api('devices/%s' % device_id)
        return Device(data, self.auth_token, self.consumer_token)

    def list_plans(self, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('plans%s' % pmtrs)
        plans = list()
        for jsoned in data['plans']:
            plan = Plan(jsoned)
            plans.append(plan)
        return plans

    def list_operating_systems(self, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('operating-systems%s' % pmtrs)
        oss = list()
        for jsoned in data['operating_systems']:
            os = OperatingSystem(jsoned)
            oss.append(os)
        return oss

    def list_ssh_keys(self, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('ssh-keys%s' % pmtrs)
        ssh_keys = list()
        for jsoned in data['ssh_keys']:
            ssh_key = SSHKey(jsoned, self.auth_token, self.consumer_token)
            ssh_keys.append(ssh_key)
        return ssh_keys

    def get_ssh_key(self, ssh_key_id):
        data = super(Manager, self).call_api('ssh-keys/%s' % ssh_key_id)
        return SSHKey(data, self.auth_token, self.consumer_token)

    def create_ssh_key(self, label, public_key):
        params = {'key': public_key, 'label': label}
        data = super(Manager, self).call_api('ssh-keys', type='POST', params=params)
        return SSHKey(data, self.auth_token, self.consumer_token)

    def list_projects(self, params={}):
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('projects%s' % pmtrs)
        self.total = data['meta']['total']
        projects = list()
        for jsoned in data['projects']:
            project = Project(jsoned, self.auth_token, self.consumer_token)
            projects.append(project)
        return projects

    def get_project(self, project_id):
        data = super(Manager, self).call_api('projects/%s' % project_id)
        return Project(data, self.auth_token, self.consumer_token)

    def create_project(self, name):
        params = {'name': name}
        data = super(Manager, self).call_api('projects', type='POST', params=params)
        return Project(data, self.auth_token, self.consumer_token)

    def list_volumes(self, project_id, params={}):
        params['include'] = 'facility'
        pmtrs = self._parse_params(params)
        data = super(Manager, self).call_api('projects/%s/storage%s' % (project_id, pmtrs))
        volumes = list()
        for jsoned in data['volumes']:
            volume = Volume(jsoned, self.auth_token, self.consumer_token)
            volumes.append(volume)
        return volumes

    def create_volume(self, project_id, description, plan, size, facility, snapshot_count=0, snapshot_frequency=None):
        params = {
            'description': description,
            'plan': plan,
            'size': size,
            'facility': facility,
        }

        if snapshot_count > 0 and snapshot_frequency is not None:
            params['snapshot_policies'] = {'snapshot_count': snapshot_count, 'snapshot_frequency': snapshot_frequency}

        data = super(Manager, self).call_api('projects/%s/storage?include=facility' % project_id, type='POST', params=params)
        return Volume(data, self.auth_token, self.consumer_token)

    def get_volume(self, volume_id):
        data = super(Manager, self).call_api('storage/%s?include=facility' % volume_id)
        return Volume(data, self.auth_token, self.consumer_token)

    def __str__(self):
        return "%s" % (self.token)

    def _parse_params(self, params):
        vals = list()
        for k, v in params.items():
            vals.append(str("%s=%s" % (k, v)))
        return "?" + "&".join(vals)
