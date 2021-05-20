# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class DeviceBatch:
    def __init__(self, data):
        self.hostname = data.get("hostname")
        self.plan = data.get("plan")
        self.operating_system = data.get("operating_system")
        self.facility = data.get("facility")
        self.metro = data.get("metro")
        self.quantity = data.get("quantity")

    def __str__(self):
        return "%s" % self.hostname
