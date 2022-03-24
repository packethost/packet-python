# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

class Usage:
    def __init__(self, data, manager):
        self.manager = manager

        self.facility = data.get("facility")
        self.type = data.get("type")
        self.name = data.get("name")
        self.plan = data.get("plan")
        self.plan_version = data.get("plan_version")
        self.quantity = data.get("quantity")
        self.unit = data.get("unit")
        self.price = data.get("price")
        self.total = data.get("total")

    def __str__(self):
        return "%s" % self.code

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.type)