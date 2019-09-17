# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Project:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data.get("id")
        self.name = data.get("name")
        self.payment_method = data.get("payment_method", [])
        self.max_projects = data.get("max_devices")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.devices = data.get("devices")
        self.invitations = data.get("invitations")
        self.memberships = data.get("memberships")
        self.members = data.get("members")
        self.ssh_keys = data.get("ssh_keys")

    def update(self):
        params = {"name": self.name}

        return self.manager.call_api(
            "projects/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("projects/%s" % self.id, type="DELETE")

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
