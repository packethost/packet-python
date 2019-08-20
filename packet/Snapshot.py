# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Snapshot:
    def __init__(self, data):
        self.id = data.get("id")
        self.status = data.get("status")
        self.timestamp = data.get("timestamp")
        self.created_at = data.get("created_at")
        self.volume = data.get("volume")

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
