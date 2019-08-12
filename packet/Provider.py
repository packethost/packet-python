# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Provider:
    def __init__(self, data):
        if data["id"] is not None:
            self.id = data["id"]
        if data["name"] is not None:
            self.name = data["name"]
        if data["status"] is not None:
            self.status = data["status"]
        if data["type"] is not None:
            self.type = data["type"]
        if data["public"] is not None:
            self.public = data["public"]

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
