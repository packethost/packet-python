# -*- coding: utf-8 -*-


class Plan():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.slug = data['slug']
        self.line = data['line']
        self.pricing = data['pricing']
        self.specs = data['specs']
        self.description = data['description']

    def __str__(self):
        return "%s" % (self.slug)

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.id)
