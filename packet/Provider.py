# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Provider:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.status = data.get("status")
        self.type = data.get("type")
        self.public = data.get("public")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
