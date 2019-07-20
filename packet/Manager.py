# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
import json

from .baseapi import BaseAPI
from .baseapi import Error as PacketError
from .Plan import Plan
from .Device import Device
from .SSHKey import SSHKey
from .Project import Project
from .Facility import Facility
from .OperatingSystem import OperatingSystem
from .Volume import Volume
from .BGPConfig import BGPConfig
from .BGPSession import BGPSession
from .IPAddress import IPAddress


class Manager(BaseAPI):
    def __init__(self, auth_token, consumer_token=None):
        super(Manager, self).__init__(auth_token, consumer_token)

    def call_api(self, method, type="GET", params=None):
        return super(Manager, self).call_api(method, type, params)

    def get_user(self):
        return self.call_api("user")

    def list_facilities(self, params={}):
        data = self.call_api("facilities", params=params)
        facilities = list()
        for jsoned in data["facilities"]:
            facility = Facility(jsoned)
            facilities.append(facility)
        return facilities

    def list_plans(self, params={}):
        data = self.call_api("plans", params=params)
        plans = list()
        for jsoned in data["plans"]:
            plan = Plan(jsoned)
            plans.append(plan)
        return plans

    def list_operating_systems(self, params={}):
        data = self.call_api("operating-systems", params=params)
        oss = list()
        for jsoned in data["operating_systems"]:
            os = OperatingSystem(jsoned)
            oss.append(os)
        return oss

    def list_projects(self, params={}):
        data = self.call_api("projects", params=params)
        self.total = data["meta"]["total"]
        projects = list()
        for jsoned in data["projects"]:
            project = Project(jsoned, self)
            projects.append(project)
        return projects

    def get_project(self, project_id):
        data = self.call_api("projects/%s" % project_id)
        return Project(data, self)

    def create_project(self, name):
        params = {"name": name}
        data = self.call_api("projects", type="POST", params=params)
        return Project(data, self)

    def list_devices(self, project_id, params={}):
        data = self.call_api("projects/%s/devices" % project_id, params=params)
        devices = list()
        for jsoned in data["devices"]:
            device = Device(jsoned, self)
            devices.append(device)
        return devices

    def create_device(
        self,
        project_id,
        hostname,
        plan,
        facility,
        operating_system,
        always_pxe=False,
        billing_cycle="hourly",
        features={},
        ipxe_script_url="",
        locked=False,
        project_ssh_keys=[],
        public_ipv4_subnet_size=31,
        spot_instance=False,
        spot_price_max=-1,
        tags={},
        termination_time=None,
        user_ssh_keys=[],
        userdata="",
    ):

        params = {
            "billing_cycle": billing_cycle,
            "facility": facility,
            "features": features,
            "hostname": hostname,
            "locked": locked,
            "operating_system": operating_system,
            "plan": plan,
            "project_id": project_id,
            "public_ipv4_subnet_size": public_ipv4_subnet_size,
            "project_ssh_keys": project_ssh_keys,
            "tags": tags,
            "user_ssh_keys": user_ssh_keys,
            "userdata": userdata,
        }

        if ipxe_script_url != "":
            params["always_pxe"] = always_pxe
            params["ipxe_script_url"] = ipxe_script_url
            params["operating_system"] = "custom_ipxe"
        if spot_instance:
            params["spot_instance"] = spot_instance
            params["spot_price_max"] = spot_price_max
            params["termination_time"] = termination_time
        data = self.call_api(
            "projects/%s/devices" % project_id, type="POST", params=params
        )
        return Device(data, self)

    def get_device(self, device_id):
        data = self.call_api("devices/%s" % device_id)
        return Device(data, self)

    def list_ssh_keys(self, params={}):
        data = self.call_api("ssh-keys", params=params)
        ssh_keys = list()
        for jsoned in data["ssh_keys"]:
            ssh_key = SSHKey(jsoned, self)
            ssh_keys.append(ssh_key)
        return ssh_keys

    def get_ssh_key(self, ssh_key_id):
        data = self.call_api("ssh-keys/%s" % ssh_key_id)
        return SSHKey(data, self)

    def create_ssh_key(self, label, public_key):
        params = {"key": public_key, "label": label}
        data = self.call_api("ssh-keys", type="POST", params=params)
        return SSHKey(data, self)

    def list_volumes(self, project_id, params={}):
        params["include"] = "facility,attachments.device"
        data = self.call_api("projects/%s/storage" % project_id, params=params)
        volumes = list()
        for jsoned in data["volumes"]:
            volume = Volume(jsoned, self)
            volumes.append(volume)
        return volumes

    def create_volume(
        self,
        project_id,
        description,
        plan,
        size,
        facility,
        snapshot_count=0,
        snapshot_frequency=None,
    ):
        params = {
            "description": description,
            "plan": plan,
            "size": size,
            "facility": facility,
        }

        if snapshot_count > 0 and snapshot_frequency is not None:
            params["snapshot_policies"] = {
                "snapshot_count": snapshot_count,
                "snapshot_frequency": snapshot_frequency,
            }

        data = self.call_api(
            "projects/%s/storage?include=facility" % project_id,
            type="POST",
            params=params,
        )

        return Volume(data, self)

    def get_volume(self, volume_id):
        params = {"include": "facility,attachments.device"}
        data = self.call_api("storage/%s" % volume_id, params=params)
        return Volume(data, self)

    def get_capacity(self, legacy=None):
        """Get capacity of all facilities.

        :param legacy: Indicate set of server types to include in response

        Validation of `legacy` is left to the packet api to avoid going out
        of date if any new value is introduced.
        The currently known values are:
          - only (current default, will be switched "soon")
          - include
          - exclude (soon to be default)
        """
        params = None
        if legacy:
            params = {"legacy": legacy}

        return self.call_api("/capacity", params=params)["capacity"]

    # servers is a list of tuples of facility, plan, and quantity.
    def validate_capacity(self, servers):
        params = {"servers": []}
        for server in servers:
            params["servers"].append(
                {
                    "facility": server[0],
                    "plan": server[1],
                    "quantity": server[2]
                 }
            )

        try:
            self.call_api("/capacity", "POST", params)
            return True
        except PacketError as e:  # pragma: no cover
            if e.args[0] == "Error 503: Service Unavailable":
                return False
            else:
                raise e

    def get_spot_market_prices(self, params={}):
        data = self.call_api("/market/spot/prices", params=params)
        return data["spot_market_prices"]

    # BGP Config
    def get_bgp_config(self, project_id):
        data = self.call_api("projects/%s/bgp-config" % project_id)
        return BGPConfig(data)

    # BGP Session
    def get_bgp_sessions(self, device_id, params={}):
        data = self.call_api("/devices/%s/bgp/sessions" % device_id,
                             type="GET", params=params)
        bgp_sessions = list()
        for jsoned in data["bgp_sessions"]:
            bpg_session = BGPSession(jsoned)
            bgp_sessions.append(bpg_session)
        return bgp_sessions

    def create_create_bgp_session(self, device_id, address_family):
        data = self.call_api("/devices/%s/bgp/sessions" % device_id,
                             type="POST",
                             params={
                                 "address_family": address_family
                                 })
        return BGPSession(data)

    # IP operations
    def list_ips(self, device_id):
        data = self.call_api("devices/%s/ips" % device_id, type="GET")
        ips = list()
        for jsoned in data["ip_addresses"]:
            ip = IPAddress(jsoned)
            ips.append(ip)
        return ips

    def get_ip(self, ip_id):
        data = self.call_api("ips/%s" % ip_id)
        return IPAddress(data)

    # Batches
    def create_batch(self,project_id, params):
        data = self.call_api("/projects/%s/devices/batch" % project_id, type="POST", params=params)
        print data