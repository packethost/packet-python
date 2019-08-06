import os
import sys
import unittest
import time
import packet


class TestDevice(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])
        self.projectId = self.manager.list_projects()[0].id

        self.device = self.manager.create_device(
            self.projectId, "devicetest", "baremetal_0", "ewr1", "centos_7"
        )

        while True:
            if self.manager.get_device(self.device.id).state == "active":
                break
            time.sleep(2)

    def test_get_device(self):
        device = self.manager.get_device(self.device.id)
        self.assertEqual(device.hostname, self.device.hostname)

    def test_list_devices(self):
        devices = self.manager.list_devices(self.projectId)
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
        bgp_session = self.manager\
            .create_bgp_session(self.device.id, address_family="ipv4")
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


if __name__ == "__main__":
    sys.exit(unittest.main())
