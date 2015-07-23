# -*- coding: utf-8 -*-
from .baseapi import BaseAPI
from .Plan import Plan
from .Device import Device
from .SSHKey import SSHKey
from .Project import Project
from .Facility import Facility
from .OperatingSystem import OperatingSystem


class Manager(BaseAPI):
    def __init__(self, auth_token, consumer_token=None):
        super(Manager, self).__init__(auth_token, consumer_token)

    def get_user(self):
        data = super(Manager, self).call_api("user")

    def list_facilities(self):
        data = super(Manager, self).call_api("facilities")
        facilities = list()
        for jsoned in data['facilities']:
            facility = Facility(jsoned)
            facilities.append(facility)
        return facilities

    def list_devices(self, project_id):
        data = super(Manager, self).call_api('projects/%s/devices' % (project_id))
        devices = list()
        for jsoned in data['devices']:
            device = Device(jsoned, self.auth_token, self.consumer_token)
            devices.append(device)
        return devices

    def create_device(self, project, hostname, plan, facility, operating_system, billing_cycle="hourly", userdata=""):
        params = {'hostname': hostname,
                  'project_id': project,
                  'plan': plan,
                  'facility': facility,
                  'operating_system': operating_system,
                  'billing_cycle': billing_cycle,
                  'userdata': userdata,
                 }
        data = super(Manager, self).call_api('projects/%s/devices' % project, type='POST', params=params)
        return Device(data, self.auth_token, self.consumer_token)

    def get_device(self, device_id):
        data = super(Manager, self).call_api('devices/%s' % device_id)
        return Device(data, self.auth_token, self.consumer_token)

    def list_plans(self):
        data = super(Manager, self).call_api('plans')
        plans = list()
        for jsoned in data['plans']:
            plan = Plan(jsoned)
            plans.append(plan)
        return plans

    def list_operating_systems(self):
        data = super(Manager, self).call_api('operating-systems')
        oss = list()
        for jsoned in data['operating_systems']:
            os = OperatingSystem(jsoned)
            oss.append(os)
        return oss

    def list_ssh_keys(self):
        data = super(Manager, self).call_api('ssh-keys')
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

    def list_projects(self):
        data = super(Manager, self).call_api('projects')
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

    def __str__(self):
        return "%s" % (self.token)
