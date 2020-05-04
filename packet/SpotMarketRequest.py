# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class SpotMarketRequest:
    def __init__(self, data):
        self.id = data.get("id")
        self.created_at = data.get("created_at")
        self.devices = data.get("devices")
        self.devices_max = data.get("devices_max")
        self.devices_min = data.get("devices_min")
        self.end_at = data.get("end_at")
        self.facilities = data.get("facilities")
        self.max_bid_price = data.get("max_bid_price")
        self.plan = data.get("plan")
        self.project = data.get("project")
        self.plan_id = data.get("plan").get("href").replace("#", "")

    def __str__(self):
        return "%s" % self.name

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
