# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Project import Project


class Batch:
    def __init__(self, data):
        if data["id"] is not None:
            self.id = data["id"]
        if data["error_messages"] is not None:
            self.error_messages = data["error_messages"]
        if data["quantity"] is not None:
            self.quantity = data["quantity"]
        if data["state"] is not None:
            self.state = data["state"]
        if data["created_at"] is not None:
            self.created_at = data["created_at"]
        if data["updated_at"] is not None:
            self.updated_at = data["updated_at"]
        if data["devices"] is not None:
            self.devices = data["devices"]
        if data["project"] is not None:
            self.project = data["project"]
        if data["state"] is not None:
            self.state = data["state"]
        if data["error_messages"] is not None:
            self.error_messages = data["error_messages"]


    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
