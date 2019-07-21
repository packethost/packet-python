import os
import sys
import unittest
import packet


class TestOrganization(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])

    def test_list_organizations(self):
        orgs = self.manager.list_organizations()
        self.assertIsNotNone(orgs)
        self.org_id = orgs[0].id

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == "__main__":
    sys.exit(unittest.main())
