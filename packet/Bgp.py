# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Bgp:
    def __init__(self, data):
        self.id = data["id"]
        self.status = data["status"]
        self.deployment_type = data["deployment_type"]
        self.asn = data["asn"]
        self.md5 = data["md5"]
        self.route_object = data["route_object"]
        self.max_prefix = data["max_prefix"]
        self.created_at = data["created_at"]
        self.requested_at = data["requested_at"]
        self.project = data["project"]
        self.sessions = data["sessions"]
        self.ranges = data["ranges"]
        self.href = data["href"]

    def __str__(self):
        return "%s" % self.code

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
