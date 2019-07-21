# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Facility import Facility


class IPAddress:
    def __init__(self, data):
        self.ip = data["id"]
        self.address_family = data["address_family"]
        self.netmask = data["netmask"]
        self.created_at = data["created_at"]
        self.details = data["details"]
        self.tags = data["tags"]
        self.public = data["public"]
        self.cidr = data["cidr"]
        self.management = data["management"]
        self.enabled = data["enabled"]
        self.global_ip = data["global_ip"]
        self.customdata = data["customdata"]
        self.project = data["project"]
        self.project_lite = data["project_lite"]
        self.facility = Facility(data["facility"])
        self.assigned_to = data["assigned_to"]
        self.interface = data["interface"]
        self.network = data["network"]
        self.address = data["address"]
        self.gateway = data["gateway"]

        def __str__(self):
            return "%s" % self.code

        def __repr__(self):
            return "{}: {}".format(self.__class__.__name__, self.id)
