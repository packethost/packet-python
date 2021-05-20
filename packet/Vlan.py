# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
from packet import Project
from .Facility import Facility
from .Metro import Metro


class Vlan:
    def __init__(self, data, manager):
        self.manager = manager
        if data is None:
            return

        self.id = data.get("id")
        self.description = data.get("description")
        self.vxlan = data.get("vxlan")
        self.internet_gateway = data.get("internet_gateway")
        self.facility_code = data.get("facility_code")
        self.metro_code = data.get("metro_code")
        self.created_at = data.get("created_at")
        facility = data.get("facility")
        self.facility = Facility(facility) if facility else None
        metro = data.get("metro")
        self.metro = Metro(metro) if metro else None

        try:
            project_data = self.manager.call_api(
                data["assigned_to"]["href"], type="GET"
            )
            self.assigned_to = Project(project_data, self.manager)
        except (KeyError, IndexError):
            self.attached_to = None

    def get(self):
        return self.manager.call_api("virtual-networks/%s" % self.id, type="GET")

    def delete(self):
        return self.manager.call_api("virtual-networks/%s" % self.id, type="DELETE")

    def create_internet_gateway(self, ip_reservation_length):
        """:param ip_reservation_length:  (required) number of IP addresses possible 8 or 16"""
        params = {"length": ip_reservation_length}
        return self.manager.call_api(
            "/virtual-networks/%s/internet-gateways" % self.id,
            type="POST",
            params=params,
        )

    def assign_native_vlan(self, port_id):
        params = {"vnid": self.id}
        return self.manager.call_api(
            "/ports/%s/native-vlan" % port_id, type="POST", params=params
        )

    def remove_native_vlan(self, port_id):
        return self.manager.call_api("/ports/%s/native-vlan" % port_id, type="DELETE")

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
