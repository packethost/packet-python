# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import os
import sys
import time
import unittest
import packet

from datetime import datetime


@unittest.skipIf(
    "PACKET_PYTHON_TEST_ACTUAL_API" not in os.environ,
    "PACKET_PYTHON_TEST_ACTUAL_API is missing from environment",
)
class TestIps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])

        org_id = cls.manager.list_organizations()[0].id
        cls.project = cls.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-IPs_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

        cls.ip_block = cls.manager.reserve_ip_address(
            project_id=cls.project.id,
            type="public_ipv4",
            quantity=1,
            facility="ewr1",
            details="delete me",
            tags=["deleteme"],
        )

        cls.device = cls.manager.create_device(
            cls.project.id, "iptest", "baremetal_0", "ewr1", "centos_7"
        )

        while True:
            if cls.manager.get_device(cls.device.id).state == "active":
                break
            time.sleep(2)

    def test_reserve_ip_address(self):
        self.assertEqual(32, self.ip_block.cidr)
        self.assertEqual("delete me", self.ip_block.details)

    def test_list_project_ips(self):
        ips = self.manager.list_project_ips(self.project.id)
        self.assertGreater(len(ips), 0)

    def test_create_device_ip(self):
        ip = self.manager.create_device_ip(
            self.device.id, address=self.ip_block.address
        )
        self.assertIsNotNone(ip)
        self.assertEqual(ip.address, self.ip_block.address)

    @classmethod
    def tearDownClass(cls):
        cls.device.delete()
        cls.ip_block.delete()
        cls.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
