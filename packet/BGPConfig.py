# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class BGPConfig:
    def __init__(self, data):
        self.id = data.get("id")
        self.status = data.get("status")
        self.deployment_type = data.get("deployment_type")
        self.asn = data.get("asn")
        self.md5 = data.get("md5")
        self.route_object = data.get("route_object")
        self.max_prefix = data.get("max_prefix")
        self.created_at = data.get("created_at")
        self.requested_at = data.get("requested_at")
        self.project = data.get("project")
        self.sessions = data.get("sessions")
        self.ranges = data.get("ranges")
        self.href = data.get("href")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
