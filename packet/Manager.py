# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only
from packet.Vlan import Vlan
from .baseapi import BaseAPI
from .baseapi import Error as PacketError
from .baseapi import ResponseError
from .Batch import Batch
from .Plan import Plan
from .Device import Device
from .SSHKey import SSHKey
from .Project import Project
from .Facility import Facility
from .Metro import Metro
from .OperatingSystem import OperatingSystem
from .Volume import Volume
from .BGPConfig import BGPConfig
from .BGPSession import BGPSession
from .IPAddress import IPAddress
from .HardwareReservation import HardwareReservation
from .Snapshot import Snapshot
from .Organization import Organization
from .Email import Email
from .Event import Event
from .Provider import Provider


class Manager(BaseAPI):
    def __init__(self, auth_token, consumer_token=None):
        super(Manager, self).__init__(auth_token, consumer_token)

    def call_api(self, method, type="GET", params=None):
        return super(Manager, self).call_api(method, type, params)

    def get_user(self):
        return self.call_api("user")

    def list_facilities(self, params={}):
        data = self.call_api("facilities", params=params)
        facilities = list()
        for jsoned in data["facilities"]:
            facility = Facility(jsoned)
            facilities.append(facility)
        return facilities

    def list_metros(self, params={}):
        data = self.call_api("locations/metros", params=params)
        metros = list()
        for jsoned in data["metros"]:
            metro = Metro(jsoned)
            metros.append(metro)
        return metros

    def list_plans(self, params={}):
        data = self.call_api("plans", params=params)
        plans = list()
        for jsoned in data["plans"]:
            plan = Plan(jsoned)
            plans.append(plan)
        return plans

    def list_operating_systems(self, params={}):
        data = self.call_api("operating-systems", params=params)
        oss = list()
        for jsoned in data["operating_systems"]:
            os = OperatingSystem(jsoned)
            oss.append(os)
        return oss

    def list_projects(self, params={}):
        data = self.call_api("projects", params=params)
        self.total = data["meta"]["total"]
        projects = list()
        for jsoned in data["projects"]:
            project = Project(jsoned, self)
            projects.append(project)
        return projects

    def get_project(self, project_id):
        data = self.call_api("projects/%s" % project_id)
        return Project(data, self)

    def create_project(self, name):
        params = {"name": name}
        data = self.call_api("projects", type="POST", params=params)
        return Project(data, self)

    def list_hardware_reservations(self, project_id, params={}):
        data = self.call_api(
            "projects/%s/hardware-reservations" % project_id, params=params
        )
        hardware_reservations = list()
        for jsoned in data["hardware_reservations"]:
            hardware_reservation = HardwareReservation(jsoned, self)
            hardware_reservations.append(hardware_reservation)
        return hardware_reservations

    def get_hardware_reservation(self, hardware_reservation_id):
        data = self.call_api("hardware-reservations/%s" % hardware_reservation_id)
        return HardwareReservation(data, self)

    def list_devices(self, project_id, params={}):
        data = self.call_api("projects/%s/devices" % project_id, params=params)
        devices = list()
        for jsoned in data["devices"]:
            device = Device(jsoned, self)
            devices.append(device)
        return devices

    def list_all_devices(self, project_id):
        raw_devices = list()
        page = 1
        while True:
            paginate = {"page": page}
            data = self.call_api("projects/%s/devices" % project_id, params=paginate)
            next = self.meta["next"]
            raw_devices.extend(data["devices"])
            if next is None:
                break
            else:
                page += 1

        all_devices = list()
        for raw_device in raw_devices:
            device = Device(raw_device, self)
            all_devices.append(device)
        return all_devices

    def create_device(
        self,
        project_id,
        hostname,
        plan,
        facility="",
        operating_system="",
        always_pxe=False,
        billing_cycle="hourly",
        features={},
        ipxe_script_url="",
        locked=False,
        project_ssh_keys=[],
        public_ipv4_subnet_size=31,
        spot_instance=False,
        spot_price_max=-1,
        tags={},
        termination_time=None,
        user_ssh_keys=[],
        userdata="",
        hardware_reservation_id="",
        storage={},
        customdata={},
        metro="",
    ):

        params = {
            "billing_cycle": billing_cycle,
            "features": features,
            "hostname": hostname,
            "locked": locked,
            "operating_system": operating_system,
            "plan": plan,
            "project_id": project_id,
            "public_ipv4_subnet_size": public_ipv4_subnet_size,
            "project_ssh_keys": project_ssh_keys,
            "tags": tags,
            "user_ssh_keys": user_ssh_keys,
            "userdata": userdata,
        }

        if metro != "":
            params["metro"] = metro
        if facility != "":
            params["facility"] = facility
        if hardware_reservation_id != "":
            params["hardware_reservation_id"] = hardware_reservation_id
        if storage:
            params["storage"] = storage
        if customdata:
            params["customdata"] = customdata
        if ipxe_script_url != "":
            params["always_pxe"] = always_pxe
            params["ipxe_script_url"] = ipxe_script_url
            params["operating_system"] = "custom_ipxe"
        if spot_instance:
            params["spot_instance"] = spot_instance
            params["spot_price_max"] = spot_price_max
            params["termination_time"] = termination_time
        data = self.call_api(
            "projects/%s/devices" % project_id, type="POST", params=params
        )
        return Device(data, self)

    def get_device(self, device_id):
        data = self.call_api("devices/%s" % device_id)
        return Device(data, self)

    def list_ssh_keys(self, params={}):
        data = self.call_api("ssh-keys", params=params)
        ssh_keys = list()
        for jsoned in data["ssh_keys"]:
            ssh_key = SSHKey(jsoned, self)
            ssh_keys.append(ssh_key)
        return ssh_keys

    def get_ssh_key(self, ssh_key_id):
        data = self.call_api("ssh-keys/%s" % ssh_key_id)
        return SSHKey(data, self)

    def create_ssh_key(self, label, public_key):
        params = {"key": public_key, "label": label}
        data = self.call_api("ssh-keys", type="POST", params=params)
        return SSHKey(data, self)

    def create_project_ssh_key(self, project_id, label, public_key):
        """
        Successfully creating an SSH key with a Project API Token results
        in a 404 from the API. If we get a 404, we try the request again.

        If the request actually failed with a 404, we will get another 404
        which we raise.

        If the request actually succeeded, we will get a 422. In this case,
        we will try to list all the keys and find the SSHKey we just
        received.

        Customer Report Reference: TUVD-0107-UIKB
        """

        def issue_req():
            try:
                params = {"key": public_key, "label": label}
                data = self.call_api(
                    "projects/%s/ssh-keys" % project_id, type="POST", params=params
                )
                return SSHKey(data, self)
            except ResponseError as e:
                if e.response.status_code == 422:
                    # Try to pluck the SSH key from the listing API
                    keys = [
                        key
                        for key in self.list_ssh_keys()
                        if key.key.strip() == public_key.strip()
                    ]
                    if len(keys) == 1:
                        return keys.pop()
                raise

        try:
            return issue_req()
        except ResponseError as e:
            if e.response.status_code == 404:
                return issue_req()
            else:
                raise

    def list_volumes(self, project_id, params={}):
        params["include"] = "facility,attachments.device"
        data = self.call_api("projects/%s/storage" % project_id, params=params)
        volumes = list()
        for jsoned in data["volumes"]:
            volume = Volume(jsoned, self)
            volumes.append(volume)
        return volumes

    def create_volume(
        self,
        project_id,
        description,
        plan,
        size,
        facility,
        snapshot_count=0,
        snapshot_frequency=None,
    ):
        params = {
            "description": description,
            "plan": plan,
            "size": size,
            "facility": facility,
        }

        if snapshot_count > 0 and snapshot_frequency is not None:
            params["snapshot_policies"] = {
                "snapshot_count": snapshot_count,
                "snapshot_frequency": snapshot_frequency,
            }

        data = self.call_api(
            "projects/%s/storage?include=facility" % project_id,
            type="POST",
            params=params,
        )

        return Volume(data, self)

    def get_volume(self, volume_id):
        params = {"include": "facility,attachments.device"}
        data = self.call_api("storage/%s" % volume_id, params=params)
        return Volume(data, self)

    def get_capacity(self, legacy=None):
        """Get capacity of all facilities.

        :param legacy: Indicate set of server types to include in response

        Validation of `legacy` is left to the packet api to avoid going out
        of date if any new value is introduced.
        The currently known values are:
          - only (current default, will be switched "soon")
          - include
          - exclude (soon to be default)
        """
        params = None
        if legacy:
            params = {"legacy": legacy}

        return self.call_api("/capacity", params=params)["capacity"]

    # servers is a list of tuples of facility, plan, and quantity.
    def validate_capacity(self, servers):
        params = {"servers": []}
        for server in servers:
            params["servers"].append(
                {"facility": server[0], "plan": server[1], "quantity": server[2]}
            )

        try:
            data = self.call_api("/capacity", "POST", params)
            return all(s["available"] for s in data["servers"])
        except PacketError as e:  # pragma: no cover
            if e.args[0] == "Error 503: Service Unavailable":
                return False
            else:
                raise e

    # servers is a list of tuples of metro, plan, and quantity.
    def validate_metro_capacity(self, servers):
        params = {"servers": []}
        for server in servers:
            params["servers"].append(
                {"metro": server[0], "plan": server[1], "quantity": server[2]}
            )

        try:
            data = self.call_api("/capacity/metros", "POST", params)
            return all(s["available"] for s in data["servers"])
        except PacketError as e:  # pragma: no cover
            if e.args[0] == "Error 503: Service Unavailable":
                return False
            else:
                raise e

    def get_spot_market_prices(self, params={}):
        data = self.call_api("/market/spot/prices", params=params)
        return data["spot_market_prices"]

    # BGP Config
    def get_bgp_config(self, project_id):
        data = self.call_api("projects/%s/bgp-config" % project_id)
        return BGPConfig(data)

    def enable_project_bgp_config(
        self, project_id, asn, deployment_type, md5=None, use_case=None
    ):
        params = {
            "deployment_type": deployment_type,
            "asn": asn,
            "md5": md5,
            "use_case": use_case,
        }
        self.call_api(
            "/projects/%s/bgp-configs" % project_id, type="POST", params=params
        )

    # BGP Session
    def get_bgp_sessions(self, device_id, params={}):
        data = self.call_api(
            "/devices/%s/bgp/sessions" % device_id, type="GET", params=params
        )
        bgp_sessions = list()
        for jsoned in data["bgp_sessions"]:
            bpg_session = BGPSession(jsoned)
            bgp_sessions.append(bpg_session)
        return bgp_sessions

    def create_bgp_session(self, device_id, address_family):
        data = self.call_api(
            "/devices/%s/bgp/sessions" % device_id,
            type="POST",
            params={"address_family": address_family},
        )
        return BGPSession(data)

    # IP operations
    def list_device_ips(self, device_id):
        data = self.call_api("devices/%s/ips" % device_id, type="GET")
        ips = list()
        for jsoned in data["ip_addresses"]:
            ip = IPAddress(jsoned, self)
            ips.append(ip)
        return ips

    def get_ip(self, ip_id):
        data = self.call_api("ips/%s" % ip_id)
        return IPAddress(data, self)

    def delete_ip(self, ip_id):
        self.call_api("ips/%s" % ip_id, type="DELETE")

    def list_project_ips(self, project_id, params={}):
        data = self.call_api("projects/%s/ips" % project_id, type="GET", params=params)
        ips = list()
        for jsoned in data["ip_addresses"]:
            ip = IPAddress(jsoned, self)
            ips.append(ip)
        return ips

    def get_available_ip_subnets(self, ip_id, cidr):
        data = self.call_api(
            "/ips/%s/available" % ip_id, type="GET", params="cidr=%s" % cidr
        )
        return data

    def create_device_ip(self, device_id, address, manageable=True, customdata=None):
        params = {
            "address": address,
            "manageable": manageable,
            "customdata": customdata,
        }

        data = self.call_api("/devices/%s/ips" % device_id, params=params, type="POST")
        return IPAddress(data, self)

    def reserve_ip_address(
        self,
        project_id,
        type,
        quantity,
        facility="",
        details=None,
        comments=None,
        tags=list(),
        metro="",
    ):
        request = {
            "type": type,
            "quantity": quantity,
            "details": details,
            "comments": comments,
            "tags": tags,
        }

        if facility != "":
            request["facility"] = facility
        if metro != "":
            request["metro"] = metro
        data = self.call_api(
            "/projects/%s/ips" % project_id, params=request, type="POST"
        )
        return IPAddress(data, self)

    # Batches
    def create_batch(self, project_id, params):
        param = {"batches": params}
        data = self.call_api(
            "/projects/%s/devices/batch" % project_id, type="POST", params=param
        )
        batches = list()
        for b in data["batches"]:
            batch = Batch(b)
            batches.append(batch)
        return batches

    def list_batches(self, project_id, params=None):
        data = self.call_api(
            "/projects/%s/batches" % project_id, type="GET", params=params
        )
        batches = list()
        for b in data["batches"]:
            batch = Batch(b)
            batches.append(batch)
        return batches

    def delete_batch(self, batch_id, remove_associated_instances=False):
        self.call_api(
            "/batches/%s" % batch_id, type="DELETE", params=remove_associated_instances
        )

    # Snapshots
    def get_snapshots(self, volume_id, params=None):
        data = self.call_api(
            "storage/%s/snapshots" % volume_id, type="GET", params=params
        )
        snapshots = list()
        for ss in data["snapshots"]:
            snapshot = Snapshot(ss)
            snapshots.append(snapshot)

        return snapshots

    def restore_volume(self, volume_id, restore_point):
        params = {"restore_point": restore_point}
        self.call_api("storage/%s/restore" % volume_id, type="POST", params=params)

    # Organization
    def list_organizations(self, params=None):
        data = self.call_api("organizations", type="GET", params=params)
        orgs = list()
        for org in data["organizations"]:
            o = Organization(org)
            orgs.append(o)

        return orgs

    def get_organization(self, org_id, params=None):
        data = self.call_api("organizations/%s" % org_id, type="GET", params=params)
        return Organization(data)

    def list_organization_projects(self, org_id, params=None):
        data = self.call_api(
            "organizations/%s/projects" % org_id, type="GET", params=params
        )
        projects = list()
        for p in data["projects"]:
            projects.append(Project(p, self))

        return projects

    def list_organization_devices(self, org_id, params=None):
        data = self.call_api(
            "organizations/%s/devices" % org_id, type="GET", params=params
        )
        devices = list()
        for d in data["devices"]:
            devices.append(Device(d, self))

        return devices

    def create_organization_project(
        self, org_id, name, payment_method_id=None, customdata=None
    ):
        params = {
            "name": name,
            "payment_method_id": payment_method_id,
            "customdata": customdata,
        }
        data = self.call_api(
            "organizations/%s/projects" % org_id, type="POST", params=params
        )
        return Project(data, self)

    # Email
    def add_email(self, address, default=False):
        params = {"address": address, "default": default}
        data = self.call_api("emails", type="POST", params=params)
        return Email(data, self)

    def get_email(self, email_id):
        data = self.call_api("emails/%s" % email_id)
        return Email(data, self)

    # Event
    def list_events(self, params=None):
        data = self.call_api("events", type="GET", params=params)
        events = list()
        for e in data["events"]:
            events.append(Event(e))

        return events

    def get_event(self, event_id):
        data = self.call_api("events/%s" % event_id)
        return Event(data)

    def list_device_events(self, device_id, params=None):
        data = self.call_api("devices/%s/events" % device_id, type="GET", params=params)
        events = list()
        for e in data["events"]:
            events.append(Event(e))

        return events

    def list_project_events(self, project_id, params=None):
        data = self.call_api(
            "projects/%s/events" % project_id, type="GET", params=params
        )
        events = list()
        for e in data["events"]:
            events.append(Event(e))

        return events

    def get_volume_events(self, volume_id, params=None):
        data = self.call_api("volumes/%s/events" % volume_id, type="GET", params=params)
        events = list()
        for e in data["events"]:
            events.append(Event(e))

        return events

    # vlan operations
    def list_vlans(self, project_id, params=None):
        data = self.call_api(
            "projects/%s/virtual-networks" % project_id, type="GET", params=params
        )
        vlans = list()
        for vlan in data["virtual_networks"]:
            vlans.append(Vlan(vlan, self))

        return vlans

    def create_vlan(
        self, project_id, facility="", vxlan=None, vlan=None, description=None, metro=""
    ):
        params = {
            "project_id": project_id,
            "vxlan": vxlan,
            "vlan": vlan,
            "description": description,
        }
        if facility != "":
            params["facility"] = facility
        if metro != "":
            params["metro"] = metro
        data = self.call_api(
            "projects/%s/virtual-networks" % project_id, type="POST", params=params
        )
        return Vlan(data, self)

    def assign_port(self, port_id, vlan_id):
        params = {"vnid": vlan_id}
        self.call_api("ports/%s/assign" % port_id, type="POST", params=params)

    def remove_port(self, port_id, vlan_id):
        params = {"vnid": vlan_id}
        self.call_api("ports/%s/unassign" % port_id, type="POST", params=params)

    def disbond_ports(self, port_id, bulk_disable):
        params = {"bulk_disable": bulk_disable}
        self.call_api("ports/%s/disbond" % port_id, type="POST", params=params)

    def bond_ports(self, port_id, bulk_disable):
        params = {"bulk_disable": bulk_disable}
        self.call_api("ports/%s/bond" % port_id, type="POST", params=params)

    def convert_layer_2(self, port_id, vlan_id):
        params = {"vnid": vlan_id}
        self.call_api("ports/%s/convert/layer-2" % port_id, type="POST", params=params)

    def convert_layer_3(self, port_id, request_ips):
        params = {"request_ips": request_ips}
        self.call_api("ports/%s/convert/layer-3" % port_id, type="POST", params=params)

    def assign_native_vlan(self, port_id, vnid):
        params = {"vnid": vnid}
        self.call_api("ports/%s/native-vlan" % port_id, type="POST", params=params)

    def remove_native_vlan(self, port_id):
        self.call_api("ports/%s/native-vlan" % port_id, type="DELETE")

    def get_vpn_configuration(self, facilityCode):
        params = {"code": facilityCode}
        data = self.call_api("user/vpn", type="GET", params=params)
        return data

    def turn_on_vpn(self):
        return self.call_api("user/vpn", type="POST")

    def turn_off_vpn(self):
        return self.call_api("user/vpn", type="DELETE")

    # Packet connect
    def create_packet_connections(self, params):
        body = {
            "name": params["name"],
            "project_id": params["project_id"],
            "provider_id": params["provider_id"],
            "provider_payload": params["provider_payload"],
            "port_speed": params["port_speed"],
            "vlan": params["vlan"],
        }
        for opt in ["tags", "description", "facility", "metro"]:
            if opt in params:
                body[opt] = params[opt]

        data = self.call_api("/packet-connect/connections", type="POST", params=body)
        return data

    def get_packet_connection(self, connection_id):
        data = self.call_api("/packet-connect/connections/%s" % connection_id)
        return data

    def delete_packet_connection(self, connection_id):
        data = self.call_api(
            "/packet-connect/connections/%s" % connection_id, type="DELETE"
        )
        return data

    def provision_packet_connection(self, connection_id):
        data = self.call_api(
            "/packet-connect/connections/{id}/provision" % connection_id, type="POST"
        )
        return data

    def deprovision_packet_connection(self, connection_id, delete):
        params = {"delete": delete}
        data = self.call_api(
            "/packet-connect/connections/{id}/deprovision" % connection_id,
            type="POST",
            params=params,
        )
        return data

    def list_packet_connect_providers(self):
        data = self.call_api("/packet-connect/providers", type="GET")
        providers = list()
        for p in data["providers"]:
            providers.append(Provider(p))
        return providers

    def get_packet_connect_provider(self, provider_id):
        data = self.call_api("/packet-connect/providers/%s" % provider_id, type="GET")
        return Provider(data)
