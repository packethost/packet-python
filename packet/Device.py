# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
# from .Volume import Volume


class Device:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data["id"]
        self.short_id = data["short_id"]
        self.hostname = data["hostname"]
        self.description = data["description"]
        self.state = data["state"]
        self.tags = data["tags"]
        if "image_url" in data:
            self.image_url = data["image_url"]
        self.billing_cycle = data["billing_cycle"]
        self.user = data["user"]
        self.iqn = data["iqn"]
        self.locked = data["locked"]
        self.bonding_mode = data["bonding_mode"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        if "ipxe_script_url" in data:
            self.ipxe_script_url = data["ipxe_script_url"]
        else:
            self.ipxe_script_url = None
        if "always_pxe" in data:
            self.always_pxe = data["always_pxe"]
        else:
            self.always_pxe = False
        if "storage" in data:
            self.storage = data["storage"]
        if "customdata" in data:
            self.customdata = data["customdata"]
        else:
            self.customdata = None
        self.operating_system = data["operating_system"]
        self.facility = data["facility"]
        self.project = data["project"]
        if "ssh_keys" in data:
            self.ssh_keys = data["ssh_keys"]
        if "project_lite" in data:
            self.project_lite = data["project_lite"]

        if "volumes" in data:
            self.volumes = data["volumes"]

        self.ip_addresses = data["ip_addresses"]
        self.plan = data["plan"]
        self.userdata = data["userdata"]
        if "switch_uuid" in data:
            self.switch_uuid = data["switch_uuid"]
        if "network_ports" in data:
            self.network_ports = data["network_ports"]
        self.href = data["href"]
        if "spot_instance" in data:
            self.spot_instance = data["spot_instance"]
        else:
            self.spot_instance = False
        if "root_password" in data:
            self.root_password = data["root_password"]

    def update(self):
        params = {
            "hostname": self.hostname,
            "locked": self.locked,
            "tags": self.tags,
            "description": self.description,
            "billing_cycle": self.billing_cycle,
            "userdata": self.userdata,
            "always_pxe": self.always_pxe,
            "ipxe_script_url": self.ipxe_script_url,
            "spot_instance": self.spot_instance,
            "customdata": self.customdata
        }

        return self.manager.call_api(
            "devices/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("devices/%s" % self.id, type="DELETE")

    def power_off(self):
        params = {"type": "power_off"}
        return self.manager.call_api(
            "devices/%s/actions" % self.id, type="POST", params=params
        )

    def power_on(self):
        params = {"type": "power_on"}
        return self.manager.call_api(
            "devices/%s/actions" % self.id, type="POST", params=params
        )

    def reboot(self):
        params = {"type": "reboot"}
        return self.manager.call_api(
            "devices/%s/actions" % self.id, type="POST", params=params
        )

    def ips(self):
        return self.manager.list_device_ips(self.id)

    def __str__(self):
        return "%s" % self.hostname

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)

    def __getitem__(self, item):
        return getattr(self, item)
