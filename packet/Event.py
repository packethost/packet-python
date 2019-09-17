# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Event:
    def __init__(self, data):
        self.id = data.get("id")
        self.type = data.get("type")
        self.body = data.get("body")
        self.state = data.get("state")
        self.created_at = data.get("created_at")
        self.modified_by = data.get("modified_by")
        self.ip = data.get("ip")
        self.interpolated = data.get("interpolated")

    def __str__(self):
        return "%s" % self.interpolated

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
