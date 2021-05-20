# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class Metro:
    def __init__(self, data):
        self.id = data.get("id")
        self.code = data.get("code")
        self.name = data.get("name")
        self.country = data.get("country")

    def __str__(self):
        return "%s" % self.code

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
