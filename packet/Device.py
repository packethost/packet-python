# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
# from .Volume import Volume
from .OperatingSystem import OperatingSystem


class Device:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data.get("id")
        self.short_id = data.get("short_id")
        self.hostname = data.get("hostname")
        self.description = data.get("description")
        self.state = data.get("state")
        self.tags = data.get("tags")
        self.image_url = data.get("image_url")
        self.billing_cycle = data.get("billing_cycle")
        self.user = data.get("user")
        self.iqn = data.get("iqn")
        self.locked = data.get("locked")
        self.bonding_mode = data.get("bonding_mode")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.ipxe_script_url = data.get("ipxe_script_url")
        self.always_pxe = data.get("always_pxe", False)
        self.storage = data.get("storage")
        self.customdata = data.get("customdata")
        self.operating_system = OperatingSystem(data["operating_system"])
        self.facility = data.get("facility")
        self.metro = data.get("metro")
        self.project = data.get("project")
        self.ssh_keys = data.get("ssh_keys")
        self.project_lite = data.get("project_lite")
        self.volumes = data.get("volumes")
        self.ip_addresses = data.get("ip_addresses")
        self.plan = data.get("plan")
        self.userdata = data.get("userdata")
        self.switch_uuid = data.get("switch_uuid")
        self.network_ports = data.get("network_ports")
        self.href = data.get("href")
        self.spot_instance = data.get("spot_instance", False)
        self.hardware_reservation_id = data.get("hardware_reservation_id")
        self.spot_price_max = data.get("spot_price_max")
        self.termination_time = data.get("termination_time")
        self.root_password = data.get("root_password")
        self.provisioning_percentage = data.get("provisioning_percentage")

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
            "customdata": self.customdata,
        }

        return self.manager.call_api(
            "devices/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("devices/%s" % self.id, type="DELETE")

    def reinstall(self, operating_system=None, ipxe_script_url=None):
        params = {"type": "reinstall"}
        if operating_system is not None:
            params["operating_system"] = operating_system
        if ipxe_script_url is not None:
            params["operating_system"] = "custom_ipxe"
            params["ipxe_script_url"] = ipxe_script_url

        return self.manager.call_api(
            "devices/%s/actions" % self.id, type="POST", params=params
        )

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

    def rescue(self):
        params = {"type": "rescue"}
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
