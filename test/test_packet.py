# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

import sys
import json
import unittest

import packet
import requests_mock


class PacketManagerTest(unittest.TestCase):
    def setUp(self):
        self.manager = PacketMockManager(auth_token="foo")

    def test_get_user(self):
        user = self.manager.get_user()

        self.assertEqual(user.get("full_name"), "Aaron Welch")

    def test_list_facilities(self):
        facilities = self.manager.list_facilities()
        for facility in facilities:
            str(facility)
            repr(facility)
            self.assertIsInstance(facility, packet.Facility)

    def test_list_metros(self):
        metros = self.manager.list_metros()
        for metro in metros:
            str(metro)
            repr(metro)
            self.assertIsInstance(metro, packet.Metro)

    def test_list_plans(self):
        plans = self.manager.list_plans()
        for plan in plans:
            str(plan)
            repr(plan)
            self.assertIsInstance(plan, packet.Plan)

    def test_list_operating_systems(self):
        oss = self.manager.list_operating_systems()
        for o in oss:
            str(o)
            repr(o)
            self.assertIsInstance(o, packet.OperatingSystem)

    def test_list_projects(self):
        projects = self.manager.list_projects()
        self.assertIsInstance(projects, list)
        for project in projects:
            str(project)
            repr(project)
            self.assertIsInstance(project, packet.Project)

    def test_get_project(self):
        project = self.manager.get_project("438659f0")
        self.assertIsInstance(project, packet.Project)

    def test_create_project(self):
        project = self.manager.create_project("test project")
        self.assertIsInstance(project, packet.Project)

    def test_update_project(self):
        name = "updated name"
        project = self.manager.get_project("438659f0")
        project.name = name
        project.update()
        self.assertEqual(project.name, name)
        self.assertIsInstance(project, packet.Project)

    def test_delete_project(self):
        project = self.manager.get_project("438659f0")
        self.assertIsNone(project.delete())

    def test_list_devices(self):
        devices = self.manager.list_devices("438659f0")
        for device in devices:
            str(device)
            repr(device)
            self.assertIsInstance(device, packet.Device)

    # TODO figure out how to properly handle this test case
    # def test_list_all_devices(self):
    #     devices = self.manager.list_all_devices("438659f0")
    #     for device in devices:
    #         str(device)
    #         repr(device)
    #         self.assertIsInstance(device, packet.Device)

    def test_create_device(self):
        device = self.manager.create_device(
            "438659f0", "hostname", "baremetal_0", "ewr1", "ubuntu_14_04"
        )
        self.assertIsInstance(device, packet.Device)

    def test_create_device_ipxe(self):
        device = self.manager.create_device(
            "438659f0",
            "hostname",
            "baremetal_0",
            "ewr1",
            "custom_ipxe",
            ipxe_script_url="https://example.com",
            always_pxe=True,
        )
        self.assertIsInstance(device, packet.Device)

    def test_get_device(self):
        device = self.manager.get_device("9dec7266")
        self.assertIsInstance(device, packet.Device)

    def test_device_actions(self):
        device = self.manager.get_device("9dec7266")
        self.assertIsNone(device.power_off())
        self.assertIsNone(device.power_on())
        self.assertIsNone(device.rescue())
        self.assertIsNone(device.reboot())

    def test_update_device(self):
        hostname = "updated hostname"
        device = self.manager.get_device("9dec7266")
        device.hostname = hostname
        device.update()
        self.assertEqual(device.hostname, hostname)
        self.assertIsInstance(device, packet.Device)

    def test_delete_device(self):
        device = self.manager.get_device("9dec7266")
        self.assertIsNone(device.delete())

    def test_list_ssh_keys(self):
        keys = self.manager.list_ssh_keys()
        for key in keys:
            str(key)
            repr(key)
            self.assertIsInstance(key, packet.SSHKey)

    def test_get_ssh_key(self):
        key = self.manager.get_ssh_key("084a5dec")
        self.assertIsInstance(key, packet.SSHKey)

    def test_create_ssh_key(self):
        public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDI4pIqzpb5g3992h+yr527VRcaB68KE4vPjWPPoiQws49KIs2NMcOzS9QE4641uW1u5ML2HgQdfYKMF/YFGnI1Y6xV637DjhDyZYV9LasUH49npSSJjsBcsk9JGfUpNAOdcgpFzK8V90eiOrOC5YncxdwwG8pwjFI9nNVPCl4hYEu1iXdyysHvkFfS2fklsNjLWrzfafPlaen+qcBxygCA0sFdW/7er50aJeghdBHnE2WhIKLUkJxnKadznfAge7oEe+3LLAPfP+3yHyvp2+H0IzmVfYvAjnzliYetqQ8pg5ZW2BiJzvqz5PebGS70y/ySCNW1qQmJURK/Wc1bt9en"

        key = self.manager.create_ssh_key(label="sshkey-name", public_key=public_key)
        self.assertIsInstance(key, packet.SSHKey)
        self.assertEqual(key.key, public_key)

    def test_delete_ssh_key(self):
        key = self.manager.get_ssh_key("084a5dec")
        self.assertIsNone(key.delete())

    def test_update_ssh_key(self):
        label = "updated label"
        key = self.manager.get_ssh_key("084a5dec")
        key.label = label
        key.update()
        self.assertEqual(key.label, label)
        self.assertIsInstance(key, packet.SSHKey)

    def test_list_volumes(self):
        volumes = self.manager.list_volumes("438659f0")
        for volume in volumes:
            self.assertIsInstance(volume, packet.Volume)

    def test_create_volume(self):
        volume = self.manager.create_volume(
            "438659f0", "volume description", "storage_0", "100", "ewr1", 7, "1day"
        )
        self.assertIsInstance(volume, packet.Volume)

    def test_get_volume(self):
        volume = self.manager.get_volume("f9a8a263")
        str(volume)
        repr(volume)
        self.assertIsInstance(volume, packet.Volume)

    def test_update_volume(self):
        description = "updated description"
        volume = self.manager.get_volume("f9a8a263")
        volume.description = description
        volume.update()
        self.assertEqual(volume.description, description)
        self.assertIsInstance(volume, packet.Volume)

    def test_delete_volume(self):
        volume = self.manager.get_volume("f9a8a263")
        self.assertIsNone(volume.delete())

    def test_list_volume_snapshots(self):
        volume = self.manager.get_volume("f9a8a263")
        snaps = volume.list_snapshots()
        for snap in snaps:
            str(snap)
            repr(snap)
            snap.delete()

    def test_attach_volume(self):
        volume = self.manager.get_volume("f9a8a263")
        self.assertIsNone(volume.attach("9dec7266"))

    def test_detach_volume(self):
        volume = self.manager.get_volume("f9a8a263")
        self.assertIsNone(volume.detach())

    def test_volume_create_snapshot(self):
        volume = self.manager.get_volume("f9a8a263")
        volume.create_snapshot()

    def test_volume_create_clone(self):
        volume = self.manager.get_volume("f9a8a263")
        volume.clone()

    def test_capacity(self):
        self.manager.get_capacity()

    def test_get_bgp_config(self):
        bgp = self.manager.get_bgp_config("1234")
        self.assertIsNotNone(bgp)

    def test_validate_capacity(self):
        capacity = self.manager.validate_capacity([("ewr1", "baremetal_0", 10)])
        self.assertTrue(capacity)

    def test_validate_metro_capacity(self):
        capacity = self.manager.validate_metro_capacity([("sv", "baremetal_1", 10)])
        self.assertTrue(capacity)

    # IP Addresses
    def test_list_device_ips(self):
        ips = self.manager.list_device_ips("e123s")
        self.assertIsNotNone(ips)

    def test_list_projects_ips(self):
        ips = self.manager.list_project_ips("438659f0")
        self.assertIsNotNone(ips)
        for ip in ips:
            self.assertIsInstance(ip.facility, packet.Facility)

    def test_list_projects_ips_state_all(self):
        ips = self.manager.list_project_ips("438659f1", params={"state": "all"})
        self.assertIsNotNone(ips)
        self.assertIsNone(ips[0].facility)
        self.assertIsInstance(ips[1].facility, packet.Facility)


class PacketMockManager(packet.Manager):
    def call_api(self, method, type="GET", params=None):
        with requests_mock.Mocker() as m:
            mock = {
                "DELETE": m.delete,
                "GET": m.get,
                "PUT": m.put,
                "POST": m.post,
                "PATCH": m.patch,
            }[type]

            if type == "DELETE":
                mock(requests_mock.ANY)
                return super(PacketMockManager, self).call_api(method, type, params)

            fixture = "%s_%s" % (type.lower(), method.lower())
            fixture = fixture.replace("/", "_").split("?")[0]
            fixture = "test/fixtures/%s.json" % fixture

            headers = {"content-type": "application/json"}

            with open(fixture) as data_file:
                j = json.load(data_file)

            mock(requests_mock.ANY, headers=headers, json=j)
            return super(PacketMockManager, self).call_api(method, type, params)


if __name__ == "__main__":
    sys.exit(unittest.main())
