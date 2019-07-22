# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Project import Project


class DeviceBatch:
    def __init__(self, data):
        self.type = data["type"] if "type" in data else None
        self.plan = data["plan"] if "plan" in data else None
        self.hostname = data["hostname"] = data["hostname"] \
            if "hostname" in data else None
        self.description = data["description"] \
            if "description" in data else None
        self.billing_cycle = data["billing_cycle"] \
            if "billing_cycle" in data else None
        self.operating_system = data["operating_system"] \
            if "operating_system" in data else None
        self.always_pxe = data["always_pxe"] if "always_pxe" in data else None
        self.userdata = data["userdata"] if "userdata" in data else None
        self.locked = data["locked"] if "locked" in data else None
        self.termination_time = data["termination_time"] \
            if "termination_time" in data else None
        self.tags = Project(data["tags"]) if "tags" in data else None
        self.project_ssh_keys = data["project_ssh_keys"] \
            if "project_ssh_keys" in data else None
        self.user_ssh_keys = data["user_ssh_keys"] \
            if "user_ssh_keys" in data else None
        self.features = data["features"] \
            if "features" in data else None
        self.customdata = data["customdata"] \
            if "customdata" in data else None
        self.ip_addresses = data["ip_addresses"] \
            if "ip_addresses" in data else None

    def __str__(self):
        return "%s" % self.type

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.type)
