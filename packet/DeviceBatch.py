# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

class DeviceBatch:
    def __init__(self, data):
        if "hostname" in data:
            self.hostname = data["hostname"]
        if "plan" in data:
            self.plan = data["plan"]
        if "operating_system" in data:
            self.operating_system = data["operating_system"]
        if "facility" in data:
            self.facility = data["facility"]
        if "quantity" in data:
            self.quantity = data["quantity"]

    def __str__(self):
        return "%s" % self.hostname
