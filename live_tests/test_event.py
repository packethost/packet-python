import os
import sys
import unittest
import packet


class TestEvent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])

        cls.events = cls.manager.list_events()

        projects = cls.manager.list_projects()
        cls.project_id = projects[0].id

    def test_list_events(self):
        self.assertTrue(len(self.events) > 0)

    def test_get_event(self):
        event = self.manager.get_event(self.events[0].id)
        self.assertEqual(event.id, self.events[0].id)

    def test_get_project_events(self):
        events = self.manager.get_project_events(self.project_id)
        self.assertTrue(len(events) > 0)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    sys.exit(unittest.main())
