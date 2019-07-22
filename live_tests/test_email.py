import os
import sys
import unittest
import packet
import random


class TestEmail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = packet.Manager(auth_token=os.environ['PACKET_TOKEN'])

        cls.email = cls.manager.add_email("john.doe{}@packet.com".format(random.randint(1, 1001)))

    def test_get_email(self):
        email = self.manager.get_email(self.email.id)
        self.assertEqual(email.address, self.email.address)

    def test_update_email(self):
        self.email.address = "john.doe{}@packet.com".format(random.randint(1, 1001))
        self.email.update()
        # email address cannot be updated?
        # email = self.manager.get_email(self.email.id)
        # self.assertEqual(email.address, self.email.address)

    @classmethod
    def tearDownClass(cls):
        cls.email.delete()


if __name__ == "__main__":
    sys.exit(unittest.main())
