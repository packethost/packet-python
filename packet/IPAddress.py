# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Facility import Facility


class IPAddress:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data.get("id")
        self.address_family = data.get("address_family")
        self.netmask = data.get("netmask")
        self.created_at = data.get("created_at")
        self.details = data.get("details")
        self.tags = data.get("tags")
        self.public = data.get("public")
        self.cidr = data.get("cidr")
        self.management = data.get("management")
        self.enabled = data.get("enabled")
        self.global_ip = data.get("global_ip")
        self.customdata = data.get("customdata")
        self.project = data.get("project")
        self.project_lite = data.get("project_lite")
        self.facility = \
            Facility(data.get("facility")) if data.get("facility") else None
        self.details = data.get("details")
        self.assigned_to = data.get("assigned_to")
        self.interface = data.get("interface")
        self.network = data.get("network")
        self.address = data.get("address")
        self.gateway = data.get("gateway")

    def delete(self):
        return self.manager.call_api("ips/%s" % self.id, type="DELETE")

    def __str__(self):
        return "%s" % self.code

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
