# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Snapshot:
    def __init__(self, data):
        if "id" in data:
            self.id = data["id"]
        if "status" in data:
            self.status = data["status"]
        if "timestamp" in data:
            self.timestamp = data["timestamp"]
        if "created_at" in data:
            self.created_at = data["created_at"]
        if "volume" in data:
            self.volume = data["volume"]

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
