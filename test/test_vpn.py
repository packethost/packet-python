# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from __future__ import print_function

import os
import sys
import unittest
import packet


@unittest.skipIf(
    "PACKET_PYTHON_TEST_ACTUAL_API" not in os.environ,
    "PACKET_PYTHON_TEST_ACTUAL_API is missing from environment",
)
class TestVpn(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])
        self.manager.turn_on_vpn()

    # def test_get_vpn_config(self):
    #     config = self.manager.get_vpn_configuration("ewr1")
    #     print(config)

    @classmethod
    def tearDownClass(self):
        self.manager.turn_off_vpn()


if __name__ == "__main__":
    sys.exit(unittest.main())
