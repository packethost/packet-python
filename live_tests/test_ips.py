import os
import time
import unittest
import packet


class TestIps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])

        cls.project_id = cls.manager.list_projects()[0].id

        cls.ipaddresses = cls.manager\
            .reserve_ip_address(project_id=cls.project_id,
                                type="global_ipv4",
                                quantity=1,
                                facility="EWR1",
                                details="delete me",
                                tags=["deleteme"])

        cls.ip = None
        for i in cls.ipaddresses:
            if i.details == "deleteme":
                cls.ip = i

        cls.device = cls.manager.create_device(
            cls.project_id, "iptest", "baremetal_0", "ewr1", "centos_7"
        )

        while True:
            if cls.manager.get_device(cls.device.id).state == "active":
                break
            time.sleep(2)

        cls.manager.reserve_ip_address(project_id=cls.project_id,
                                       type="global_ipv4",
                                       quantity=1,
                                       facility="EWR1")

    def list_project_ips(self):
        ips = self.manager.list_project_ips(self.project_id)

        self.assertIsNotNone(ips)

    def test_create_device_ip(self):
        ipaddress = self.manager.create_device_ip(self.device.id,
                                                  address="147.75.39.190")
        self.assertIsNotNone(ipaddress)

    @classmethod
    def tearDownClass(cls):
        cls.device.delete()
