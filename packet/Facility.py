# -*- coding: utf-8 -*-


class Facility():
    def __init__(self, data):
        self.id = data['id']
        self.code = data['code']
        self.name = data['name']
        self.features = data['features']
        self.address = data['address']

    def __str__(self):
        return "%s" % self.name
