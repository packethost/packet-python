# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class BGPSession:
    def __init__(self, data):
        self.id = data.get("id")
        self.status = data.get("status")
        self.learned_routes = data.get("learned_routes")
        self.switch_name = data.get("switch_name")
        self.default_route = data.get("default_route")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.device = data.get("device")
        self.address_family = data.get("address_family")
        self.href = data.get("href")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
