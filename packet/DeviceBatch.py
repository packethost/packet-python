# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
import json

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

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        type = from_str(obj.get(u"type"))
        plan = from_str(obj.get(u"plan"))
        hostname = from_str(obj.get(u"hostname"))
        hostnames = from_str(obj.get(u"hostnames"))
        description = from_str(obj.get(u"description"))
        billing_cycle = from_str(obj.get(u"billing_cycle"))
        operating_system = from_str(obj.get(u"operating_system"))
        always_pxe = from_str(obj.get(u"always_pxe"))
        userdata = from_str(obj.get(u"userdata"))
        locked = from_str(obj.get(u"locked"))
        termination_time = from_str(obj.get(u"termination_time"))
        tags = from_str(obj.get(u"tags"))
        project_ssh_keys = from_str(obj.get(u"project_ssh_keys"))
        user_ssh_keys = from_str(obj.get(u"user_ssh_keys"))
        features = from_str(obj.get(u"features"))
        customdata = from_str(obj.get(u"customdata"))
        ip_addresses = from_str(obj.get(u"ip_addresses"))
        return Batch(type, plan, hostname, hostnames, description, billing_cycle, operating_system, always_pxe, userdata, locked, termination_time, tags, project_ssh_keys, user_ssh_keys, features, customdata, ip_addresses)

    def to_dict(self):
        result = {}
        result[u"type"] = from_str(self.type)
        result[u"plan"] = from_str(self.plan)
        result[u"hostname"] = from_str(self.hostname)
        result[u"hostnames"] = from_str(self.hostnames)
        result[u"description"] = from_str(self.description)
        result[u"billing_cycle"] = from_str(self.billing_cycle)
        result[u"operating_system"] = from_str(self.operating_system)
        result[u"always_pxe"] = from_str(self.always_pxe)
        result[u"userdata"] = from_str(self.userdata)
        result[u"locked"] = from_str(self.locked)
        result[u"termination_time"] = from_str(self.termination_time)
        result[u"tags"] = from_str(self.tags)
        result[u"project_ssh_keys"] = from_str(self.project_ssh_keys)
        result[u"user_ssh_keys"] = from_str(self.user_ssh_keys)
        result[u"features"] = from_str(self.features)
        result[u"customdata"] = from_str(self.customdata)
        result[u"ip_addresses"] = from_str(self.ip_addresses)
        return result


class Batches:
    def __init__(self, batches):
        self.batches = batches

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        batches = from_list(DeviceBatch.from_dict, obj.get(u"batches"))
        return Batches(batches)

    def to_dict(self):
        result = {u"batches": from_list(lambda x: to_class(DeviceBatch, x),
                                        self.batches)}
        return result


def batches_from_dict(s):
    return Batches.from_dict(s)


def batches_to_dict(x):
    return to_class(Batches, x)


def from_str(x):
    assert isinstance(x, (str, unicode))
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()
