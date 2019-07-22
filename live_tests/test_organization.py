import os
import sys
import unittest
import packet


class TestOrganization(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])
        orgs = self.manager.list_organizations()
        self.org_id = orgs[0].id

    def test_organization(self):
        org = self.manager.get_organization(org_id=self.org_id)
        self.assertEquals(self.org_id, org.id)

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == "__main__":
    sys.exit(unittest.main())
