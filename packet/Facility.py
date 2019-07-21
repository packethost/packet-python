# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

class Facility:
    def __init__(self, data):
        if "id" in data:
            self.id = data["id"]
        if "code" in data:
            self.code = data["code"]
        if "name" in data:
            self.name = data["name"]
        if "features" in data:
            self.features = data["features"]
        if "address" in data:
            self.address = data["address"]

    def __str__(self):
        return "%s" % self.code

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
