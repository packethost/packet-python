# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class OperatingSystem(object):
    def __init__(self, data):
        self.slug = data.get("slug")
        self.name = data.get("name")
        self.distro = data.get("distro")
        self.version = data.get("version")
        self.provisionable_on = data.get("provisionable_on")

    def __str__(self):
        return "%s %s %s %s" % (self.slug, self.name, self.distro, self.version)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.slug)
