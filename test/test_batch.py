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
class TestBatches(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])
        org_id = self.manager.list_organizations()[0].id
        self.project = self.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-Batch_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )
        self.batches = list()

    def test_create_batch(self):
        params = list()
        batch01 = packet.DeviceBatch(
            {
                "hostname": "batchtest01",
                "quantity": 1,
                "facility": "ewr1",
                "operating_system": "centos_7",
                "plan": "baremetal_0",
            }
        )

        params.append(batch01)
        data = self.manager.create_batch(project_id=self.project.id, params=params)
        self.batches = data
        time.sleep(10)

    def test_list_batches(self):
        self.manager.list_batches(project_id=self.project.id)

    def test_delete_batches(self):
        self.batches = self.manager.list_batches(project_id=self.project.id)
        for batch in self.batches:
            self.manager.delete_batch(batch.id, remove_associated_instances=True)

    @classmethod
    def tearDownClass(self):
        devices = self.manager.list_devices(project_id=self.project.id)
        for device in devices:
            if device.hostname == "batchtest01":
                if device.state != "active":
                    while True:
                        if self.manager.get_device(device.id).state != "active":
                            time.sleep(2)
                        else:
                            device.delete()
                            break
        self.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
