# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Event:
    def __init__(self, data):
        self.id = data["id"]
        self.type = data["type"]
        self.body = data["body"]
        self.state = data["state"]
        self.created_at = data["created_at"]
        self.modified_by = data["modified_by"]
        self.ip = data["ip"]
        self.interpolated = data["interpolated"]

    def __str__(self):
        return "%s" % self.interpolated

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
