# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Plan:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.slug = data.get("slug")
        self.line = data.get("line")
        self.pricing = data.get("pricing")
        self.specs = data.get("specs")
        self.description = data.get("description")
        self.available_in = data.get("available_in")

    def __str__(self):
        return "%s" % self.slug

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
