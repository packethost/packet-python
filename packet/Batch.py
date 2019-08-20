# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Batch:
    def __init__(self, data):
        self.id = data.get("id")
        self.error_messages = data.get("error_messages")
        self.quantity = data.get("quantity")
        self.state = data.get("state")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.devices = data.get("devices")
        self.project = data.get("project")
        self.state = data.get("state")
        self.error_messages = data.get("error_messages")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
