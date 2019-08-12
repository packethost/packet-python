# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Email:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data["id"]
        self.address = data["address"]
        self.default = data["default"]
        self.verified = data["verified"]

    def update(self):
        params = {"address": self.address, "default": self.default}

        return self.manager.call_api(
            "emails/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("emails/%s" % self.id, type="DELETE")

    def __str__(self):
        return "%s" % self.address

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
