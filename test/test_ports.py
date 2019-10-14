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
class TestPorts(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])

        org_id = self.manager.list_organizations()[0].id
        self.project = self.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-Ports_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

        self.device = self.manager.create_device(
            self.project.id, "networktestingdevice", "baremetal_2", "ewr1", "centos_7"
        )
        self.vlan = self.manager.create_vlan(self.project.id, "ewr1")
        self.vlan2 = self.manager.create_vlan(self.project.id, "ewr1")

        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(2)
        self.device_port_id = self.device["network_ports"][0]["id"]
        self.device_eth0_port_id = self.device["network_ports"][1]["id"]

    def test01_convert_layer2(self):
        self.manager.convert_layer_2(self.device_port_id, self.vlan.id)

    def test02_remove_port(self):
        self.manager.remove_port(self.device_port_id, self.vlan.id)

    def test03_assign_port(self):
        self.manager.assign_port(self.device_port_id, self.vlan.id)

    def test04_bond_port(self):
        self.manager.bond_ports(self.device_port_id, False)

    def test05_disbond_port(self):
        self.manager.disbond_ports(self.device_port_id, False)

    def test06_assign_native_vlan(self):
        # must remove vlan from any previous association and attach more than one vlan to the eth0 port to be able to
        #  choose a native vlan
        self.manager.remove_port(self.device_port_id, self.vlan.id)
        self.manager.assign_port(self.device_eth0_port_id, self.vlan.id)
        self.manager.assign_port(self.device_eth0_port_id, self.vlan2.id)
        self.manager.assign_native_vlan(self.device_eth0_port_id, self.vlan.id)

    def test07_remove_native_vlan(self):
        self.manager.remove_native_vlan(self.device_eth0_port_id)

    def test08_convert_layer3(self):
        ipadresses = list({"address_family": 6, "public": False})
        self.manager.convert_layer_3(self.device_port_id, ipadresses)

    @classmethod
    def tearDownClass(self):
        self.manager.remove_port(self.device_eth0_port_id, self.vlan.id)
        self.device.delete()
        self.vlan2.delete()
        self.vlan.delete()
        self.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
