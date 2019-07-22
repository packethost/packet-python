# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Device import Device


class BGPSession:
    def __init__(self, data):
        self.id = data["id"]
        self.status = data["status"]
        self.learned_routes = data["learned_routes"]
        self.switch_name = data["switch_name"]
        self.default_route = data["default_route"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.device = data["device"]
        self.address_family = data["address_family"]
        self.href = data["href"]

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
