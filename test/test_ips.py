import os
import time
import unittest
import packet

from datetime import datetime


class TestIps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ['PACKET_AUTH_TOKEN'])

        org_id = cls.manager.list_organizations()[0].id
        cls.project = cls.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-IPs_{}".format(datetime.utcnow().timestamp())
        )

        cls.ipaddresses = cls.manager\
            .reserve_ip_address(project_id=cls.project.id,
                                type="global_ipv4",
                                quantity=1,
                                facility="EWR1",
                                details="delete me",
                                tags=["deleteme"])

        cls.device = cls.manager.create_device(
            cls.project.id, "iptest", "baremetal_0", "ewr1", "centos_7"
        )

        while True:
            if cls.manager.get_device(cls.device.id).state == "active":
                break
            time.sleep(2)

        cls.manager.reserve_ip_address(project_id=cls.project.id,
                                       type="global_ipv4",
                                       quantity=1,
                                       facility="ewr1")

    def list_project_ips(self):
        ips = self.manager.list_project_ips(self.project.id)

        self.assertIsNotNone(ips)

    def test_create_device_ip(self):
        ip = None
        params = {
            "include": ["facility"]
        }
        ips = self.manager.list_project_ips(self.project.id,
                                            params=params)
        for i in ips:
            if i.facility.code == "ewr1" \
                    and i.address_family == 4:
                ip = i
                break

        ipaddress = self.manager.create_device_ip(self.device.id,
                                                  address=ip.address)
        self.assertIsNotNone(ipaddress)

    @classmethod
    def tearDownClass(cls):
        cls.device.delete()
        cls.project.delete()
