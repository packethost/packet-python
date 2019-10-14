# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import os
import sys
import unittest
import packet


@unittest.skipIf(
    "PACKET_PYTHON_TEST_ACTUAL_API" not in os.environ,
    "PACKET_PYTHON_TEST_ACTUAL_API is missing from environment",
)
class TestOrganization(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])
        orgs = self.manager.list_organizations()
        self.org_id = orgs[0].id

    def test_organization(self):
        org = self.manager.get_organization(org_id=self.org_id)
        self.assertEqual(self.org_id, org.id)

    def test_create_organization_project(self):
        project = self.manager.create_organization_project(
            org_id=self.org_id,
            name="live-tests-project",
            payment_method_id=None,
            customdata={"tag": "delete me"},
        )
        self.assertIsNotNone(project)
        project.delete()

    def test_list_organization_projects(self):
        projects = self.manager.list_organization_projects(org_id=self.org_id)
        self.assertGreater(len(projects), 0)

    def test_list_organization_devices(self):
        devices = self.manager.list_organization_devices(org_id=self.org_id)
        self.assertGreaterEqual(len(devices), 0)

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == "__main__":
    sys.exit(unittest.main())
