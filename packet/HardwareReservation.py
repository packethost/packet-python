# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Plan import Plan
from .Project import Project
from .Device import Device


class HardwareReservation:
    def __init__(self, data, manager):
        self.manager = manager

        self.id = data.get("id")
        self.created_at = data.get("created_at")
        self.billing_cycle = data.get("billing_cycle")
        self.created_at = data.get("created_at")
        self.short_id = data.get("short_id")
        self.intervals = data.get("intervals")
        self.current_period = data.get("current_period")
        self.started_at = data.get("started_at")
        self.custom_rate = data.get("custom_rate")
        self.remove_at = data.get("remove_at")
        self.project = data.get("project")
        # self.facility = data.get("facility")
        self.device = data.get("device")
        self.provisionable = data.get("provisionable")
        self.spare = data.get("spare")
        self.need_of_service = data.get("need_of_service")
        self.plan = Plan(data.get("plan"))
        self.switch_uuid = data.get("switch_uuid")

        try:
            project_data = self.manager.call_api(data["project"]["href"], type="GET")
            self.project = Project(project_data, self.manager)
        except (KeyError, IndexError):
            self.attached_to = None

        # endpoint is not working yet
        # try:
        #     facility_data = self.manager.call_api(
        #         data["facility"]["href"], type="GET"
        #     )
        #     self.project = Facility(facility_data, self.manager)
        # except (KeyError, IndexError):
        #     self.attached_to = None

        try:
            device_data = self.manager.call_api(data["device"]["href"], type="GET")
            self.device = Device(device_data, self.manager)
        except (KeyError, IndexError, TypeError):
            self.attached_to = None

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)

    def __getitem__(self, item):
        return getattr(self, item)
