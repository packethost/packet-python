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
class TestDevice(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])
        org_id = self.manager.list_organizations()[0].id
        self.project = self.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-Device_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

        self.manager.enable_project_bgp_config(
            project_id=self.project.id, deployment_type="local", asn=65000
        )

        self.device = self.manager.create_device(
            self.project.id, "devicetest", "baremetal_0", "ewr1", "centos_7"
        )

        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(2)

    def test_get_device(self):
        device = self.manager.get_device(self.device.id)
        self.assertEqual(device.hostname, self.device.hostname)

    def test_list_devices(self):
        devices = self.manager.list_devices(self.project.id)
        for device in devices:
            if device.id is self.device.id:
                break
        self.assertRaises(TypeError)

    def test_update_device(self):
        self.device.hostname = "newname"
        self.device.update()
        device = self.manager.get_device(self.device.id)
        self.assertEqual(self.device.hostname, device.hostname)

    def test_create_bgp_session(self):
        bgp_session = self.manager.create_bgp_session(
            self.device.id, address_family="ipv4"
        )
        self.assertIsNotNone(bgp_session)

    def test_get_bgp_sessions(self):
        data = self.manager.get_bgp_sessions(self.device.id)
        self.assertIsNotNone(self, data)

    def test_get_device_events(self):
        events = self.manager.list_device_events(self.device.id)
        self.assertGreater(len(events), 0)

    def test_get_device_ips(self):
        ips = self.device.ips()
        self.assertTrue(len(ips) > 0)

    @classmethod
    def tearDownClass(self):
        self.device.delete()
        self.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
