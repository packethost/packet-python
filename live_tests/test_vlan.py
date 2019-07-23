import os
import sys
import unittest
import packet


class TestVlan(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])
        self.projectId = self.manager.list_projects()[0].id

        self.vlan = self.manager.create_vlan(self.projectId, "ewr1")

    def test_list_vlan(self):
        vlans = self.manager.list_vlans(self.projectId)
        self.assertTrue(len(vlans) > 0)

    def test_get_vlan(self):
        vlan = self.vlan.get()
        self.assertEqual(vlan['id'], self.vlan.id)

    # todo: ucomment below maybe test with a device's vlan
    # self.vlan.create_internet_gateway("8")
    # todo: add assign remove port tests
   # def test_create_internet_gateway(self):

    @classmethod
    def tearDownClass(self):
        self.vlan.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
