# -*- coding: utf-8 -*-

class OperatingSystem():
    def __init__(self, data):
        self.slug = data['slug']
        self.name = data['name']
        self.distro = data['distro']
        self.version = data['version']

    def __str__(self):
        return "%s %s %s %s" % (self.slug, self.name, self.distro, self.version)
