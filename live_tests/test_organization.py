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
    #
    # def test_get_organization(self):
    #     print self.org_id
    #     organization = self.manager.get_organization(self.org_id)
    #     self.assertIsNotNone(organization)
    #     self.assertEquals(self.org_id, organization.id)

    @classmethod
    def tearDownClass(self):
        print "tada"

if __name__ == "__main__":
    sys.exit(unittest.main())
