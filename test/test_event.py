# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import os
import sys
import unittest
import packet

from datetime import datetime


@unittest.skipIf(
    "PACKET_PYTHON_TEST_ACTUAL_API" not in os.environ,
    "PACKET_PYTHON_TEST_ACTUAL_API is missing from environment",
)
class TestEvent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ["PACKET_AUTH_TOKEN"])

        cls.events = cls.manager.list_events()

        org_id = cls.manager.list_organizations()[0].id
        cls.project = cls.manager.create_organization_project(
            org_id=org_id,
            name="Int-Tests-Events_{}".format(
                datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
            ),
        )

    def test_list_events(self):
        self.assertTrue(len(self.events) > 0)

    def test_get_event(self):
        event = self.manager.get_event(self.events[0].id)
        self.assertEqual(event.id, self.events[0].id)

    def test_get_project_events(self):
        events = self.manager.list_project_events(self.project.id)
        self.assertGreaterEqual(len(events), 0)

    @classmethod
    def tearDownClass(cls):
        cls.project.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
