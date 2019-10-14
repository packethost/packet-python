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
class TestVlan(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])

        org_id = self.manager.list_organizations()[0].id
        self.project = self.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-VLAN_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

        self.device = self.manager.create_device(
            self.project.id, "vlantesting", "baremetal_2", "ewr1", "centos_7"
        )

        self.vlan = self.manager.create_vlan(self.project.id, "ewr1")
        self.vlan2 = self.manager.create_vlan(self.project.id, "ewr1")
        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(2)
        self.device_port_id = self.device["network_ports"][0]["id"]
        self.device_eth0_port_id = self.device["network_ports"][1]["id"]
        # must convert to layer 2 to work with vlans
        self.manager.convert_layer_2(self.device_port_id, self.vlan.id)

    def test_list_vlan(self):
        vlans = self.manager.list_vlans(self.project.id)
        self.assertTrue(len(vlans) > 0)

    def test_get_vlan(self):
        vlan = self.vlan.get()
        self.assertEqual(vlan["id"], self.vlan.id)

    def test_assign_port(self):
        self.manager.disbond_ports(self.device_eth0_port_id, False)
        self.manager.remove_port(self.device_port_id, self.vlan.id)
        self.manager.assign_port(self.device_eth0_port_id, self.vlan.id)
        self.manager.assign_port(self.device_eth0_port_id, self.vlan2.id)
        self.vlan.assign_native_vlan(self.device_eth0_port_id)

    def test_remove_port(self):
        self.vlan.remove_native_vlan(self.device_eth0_port_id)

    @classmethod
    def tearDownClass(self):
        self.device.delete()
        self.vlan.delete()
        self.vlan2.delete()
        self.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
