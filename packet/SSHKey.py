# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class SSHKey:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data.get("id")
        self.key = data.get("key")
        self.label = data.get("label")
        self.fingerprint = data.get("fingerprint")
        self.href = data.get("href")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

        try:
            self.owner = data["owner"]["href"]
        except (KeyError, TypeError):
            self.owner = None

    def update(self):
        params = {"label": self.label, "key": self.key}

        return self.manager.call_api(
            "ssh-keys/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("ssh-keys/%s" % self.id, type="DELETE")

    def __str__(self):
        return "%s %s" % (self.id, self.label)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
