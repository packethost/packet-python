import sys
import json
import unittest
import packet


class PacketManagerTest(unittest.TestCase):
    def setUp(self):
        self.manager = PacketMockManager(auth_token="foo")

    def test_get_user(self):
        user = self.manager.get_user()
        self.assertEqual(user.get('full_name'), 'Aaron Welch')

    def test_list_facilities(self):
        facilities = self.manager.list_facilities()
        for facility in facilities:
            str(facility)
            repr(facility)
            self.assertIsInstance(facility, packet.Facility)

    def test_list_plans(self):
        plans = self.manager.list_plans()
        for plan in plans:
            str(plan)
            repr(plan)
            self.assertIsInstance(plan, packet.Plan)

    def test_list_operating_systems(self):
        oss = self.manager.list_operating_systems()
        for os in oss:
            str(os)
            repr(os)
            self.assertIsInstance(os, packet.OperatingSystem)

    def test_list_projects(self):
        projects = self.manager.list_projects()
        self.assertTrue(isinstance(projects, list))
        for project in projects:
            str(project)
            repr(project)
            self.assertIsInstance(project, packet.Project)

    def test_get_project(self):
        project = self.manager.get_project('438659f0')
        self.assertIsInstance(project, packet.Project)

    def test_create_project(self):
        project = self.manager.create_project('test project')
        self.assertIsInstance(project, packet.Project)

    def test_update_project(self):
        name = 'updated name'
        project = self.manager.get_project('438659f0')
        project.name = name
        project.update()
        self.assertEqual(project.name, name)
        self.assertIsInstance(project, packet.Project)

    def test_delete_project(self):
        project = self.manager.get_project('438659f0')
        self.assertTrue(project.delete())

    def test_list_devices(self):
        devices = self.manager.list_devices('438659f0')
        for device in devices:
            str(device)
            repr(device)
            self.assertIsInstance(device, packet.Device)

    def test_create_device(self):
        device = self.manager.create_device('438659f0', 'hostname', 'baremetal_0', 'ewr1', 'ubuntu_14_04')
        self.assertIsInstance(device, packet.Device)

    def test_get_device(self):
        device = self.manager.get_device('9dec7266')
        self.assertIsInstance(device, packet.Device)

    def test_device_actions(self):
        device = self.manager.get_device('9dec7266')
        self.assertTrue(device.power_off() is None)
        self.assertTrue(device.power_on() is None)
        self.assertTrue(device.reboot() is None)

    def test_update_device(self):
        hostname = 'updated hostname'
        device = self.manager.get_device('9dec7266')
        device.hostname = hostname
        device.update()
        self.assertEqual(device.hostname, hostname)
        self.assertIsInstance(device, packet.Device)

    def test_delete_device(self):
        device = self.manager.get_device('9dec7266')
        self.assertTrue(device.delete())

    def test_list_ssh_keys(self):
        keys = self.manager.list_ssh_keys()
        for key in keys:
            str(key)
            repr(key)
            self.assertIsInstance(key, packet.SSHKey)

    def test_get_ssh_key(self):
        key = self.manager.get_ssh_key('084a5dec')
        self.assertIsInstance(key, packet.SSHKey)

    def test_create_ssh_key(self):
        public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI4pIqzpb5g3992h+yr527VRcaB68KE4vPjWPPoiQws49KIs2NMcOzS9QE4\
641uW1u5ML2HgQdfYKMF/YFGnI1Y6xV637DjhDyZYV9LasUH49npSSJjsBcsk9JGfUpNAOdcgpFzK8V90eiOrOC5YncxdwwG8pwjFI9nNVPCl4hYEu1iXdy\
ysHvkFfS2fklsNjLWrzfafPlaen+qcBxygCA0sFdW/7er50aJeghdBHnE2WhIKLUkJxnKadznfAge7oEe+3LLAPfP+3yHyvp2+H0IzmVfYvAjnzliYetqQ8\
pg5ZW2BiJzvqz5PebGS70y/ySCNW1qQmJURK/Wc1bt9en"
        key = self.manager.create_ssh_key(label="sshkey-name", public_key=public_key)
        self.assertIsInstance(key, packet.SSHKey)
        self.assertEquals(key.key, public_key)

    def test_delete_ssh_key(self):
        key = self.manager.get_ssh_key('084a5dec')
        self.assertTrue(key.delete())

    def test_update_ssh_key(self):
        label = 'updated label'
        key = self.manager.get_ssh_key('084a5dec')
        key.label = label
        key.update()
        self.assertEqual(key.label, label)
        self.assertIsInstance(key, packet.SSHKey)

    def test_list_volumes(self):
        volumes = self.manager.list_volumes('438659f0')
        for volume in volumes:
            self.assertIsInstance(volume, packet.Volume)

    def test_create_volume(self):
        volume = self.manager.create_volume('438659f0', 'volume description', 'storage_0', '100', 'ewr1', 7, '1day')
        self.assertIsInstance(volume, packet.Volume)

    def test_get_volume(self):
        volume = self.manager.get_volume('f9a8a263')
        str(volume)
        repr(volume)
        self.assertIsInstance(volume, packet.Volume)

    def test_update_volume(self):
        description = 'updated description'
        volume = self.manager.get_volume('f9a8a263')
        volume.description = description
        volume.update()
        self.assertEqual(volume.description, description)
        self.assertIsInstance(volume, packet.Volume)

    def test_delete_volume(self):
        volume = self.manager.get_volume('f9a8a263')
        self.assertTrue(volume.delete())

    def test_list_volume_snapshots(self):
        volume = self.manager.get_volume('f9a8a263')
        snaps = volume.list_snapshots()
        for snap in snaps:
            str(snap)
            repr(snap)
            snap.delete()

    def test_attach_volume(self):
        volume = self.manager.get_volume('f9a8a263')
        self.assertTrue(volume.attach('9dec7266') is None)

    def test_detach_volume(self):
        volume = self.manager.get_volume('f9a8a263')
        self.assertTrue(volume.detach())

    def test_volume_create_snapshot(self):
        volume = self.manager.get_volume('f9a8a263')
        volume.create_snapshot()


class PacketMockManager(packet.Manager):

    def call_api(self, method, type='GET', params=None):
        if type == 'DELETE':
            return True
        else:
            fixture = '%s_%s' % (type.lower(), method.lower())
            with open('fixtures/%s.json' % (fixture.replace('/', '_').split("?")[0])) as data_file:
                return json.load(data_file)

if __name__ == '__main__':
    sys.exit(unittest.main())
