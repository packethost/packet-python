# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import os
import sys
import unittest
import time
import packet

from datetime import datetime


@unittest.skipIf(
    "PACKET_PYTHON_TEST_ACTUAL_API" not in os.environ,
    "PACKET_PYTHON_TEST_ACTUAL_API is missing from environment",
)
class TestVolume(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.timestamp = ""
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])
        self.projectId = self.manager.list_projects()[0].id

        org_id = self.manager.list_organizations()[0].id
        self.project = self.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-Volume_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

        self.volume = self.manager.create_volume(
            self.project.id, "volume description", "storage_1", "100", "ewr1", 7, "1day"
        )

        while True:
            if self.manager.get_volume(self.volume.id).state == "active":
                break
            time.sleep(2)

        self.device = self.manager.create_device(
            self.project.id, "devicevolumestest", "baremetal_0", "ewr1", "centos_7"
        )

        self.policy = self.volume.create_snapshot_policy("1day", 2)
        self.clone = self.volume.clone()

        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(2)

    def test_get_volume(self):
        volume = self.manager.get_volume(self.volume.id)
        self.assertEqual(volume.description, self.volume.description)

    def test_list_volumes(self):
        volumes = self.manager.list_volumes(self.project.id)
        for volume in volumes:
            if volume.id is self.volume.id:
                break
        self.assertRaises(TypeError)

    def test_update_volume(self):
        self.volume.description = "newdescription"
        self.volume.update()
        volume = self.manager.get_volume(self.volume.id)
        self.assertEqual(self.volume.description, volume.description)

    def test_attach_volume(self):
        self.volume.attach(self.device.id)
        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(1)

    def test_detach_volume(self):
        self.volume.detach()
        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(1)

    def test_create_snapshot(self):
        self.volume.create_snapshot()

    def test_get_snapshots(self):
        snapshots = self.manager.get_snapshots(self.volume.id)
        self.assertIsNotNone(snapshots)
        self.__class__.timestamp = snapshots[0].timestamp

    def test_update_snapshot_policy(self):
        self.policy = self.policy.update_snapshot_policy("1month", 3)
        assert self.policy.frequency == "1month"
        assert self.policy.count == 3

    def test_restore_volume(self):
        self.volume.restore(self.__class__.timestamp)

    @classmethod
    def tearDownClass(self):
        self.policy.delete()
        self.volume.delete()
        self.device.delete()
        self.clone.delete()
        self.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
