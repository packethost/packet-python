import os
import sys
import time
import unittest
import packet


class TestBatches(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])
        self.projectId = self.manager.list_projects()[0].id
        self.batches = list()

    def test_create_batch(self):
        params = list()
        batch01 = packet.DeviceBatch({
            "hostname": "batchtest01",
            "quantity": 1,
            "facility": "ewr1",
            "operating_system": "centos_7",
            "plan": "baremetal_0",
        })

        params.append(batch01)
        batch02 = packet.DeviceBatch({
            "hostname": "batchtest02",
            "quantity": 1,
            "facility": "ewr1",
            "operating_system": "centos_7",
            "plan": "baremetal_0",
        })
        params.append(batch02)
        data = self.manager.create_batch(project_id=self.projectId,
                                         params=params)
        self.batches = data
        time.sleep(10)

    def test_list_batches(self):
        self.manager.list_batches(project_id=self.projectId)

    def test_delete_batches(self):
        self.batches = self.manager.list_batches(project_id=self.projectId)
        for batch in self.batches:
                self.manager.delete_batch(batch.id,
                                          remove_associated_instances=True)

    @classmethod
    def tearDownClass(self):
        devices = self.manager.list_devices(project_id=self.projectId)
        for device in devices:
            if device.hostname == "hostname01" \
                    or device.hostname == "hostname02":
                if device.state != "active":
                    while True:
                        if self.manager\
                                .get_device(self.device.id).state == "active":
                            break
                        time.sleep(2)
                    device.delete()
                device.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
