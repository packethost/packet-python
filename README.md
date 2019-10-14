# Packet

A Python client for the Packet API.

![Build Status](https://drone.packet.net/api/badges/packethost/packet-python/status.svg "Build Status")

## Table of Contents

* [Installation](#installation)
* [Documentation](#documentation)
* [Authentication](#authentication)
* [Examples](#examples)
  * [List Projects](#list-projects)
  * [List Plans](#list-plans)
  * [Creating a Device](#creating-a-device)
  * [Checking the Status and Rebooting a Device](#checking-the-status-and-rebooting-a-device)
  * [Listing all Devices Limiting to 50 per Page](#listing-all-devices-limiting-to-50-per-page)
  * [Updating a Device](#updating-a-device)
  * [Deleting a Device](#deleting-a-device)
  * [Creating a Device Batch](#creating-a-device-batch)
  * [Creating a Volume](#creating-a-volume)
  * [Attaching and Detaching a Volume](#attaching-and-detaching-a-volume)
  * [Creating and Restoring a Volume Snapshot](#creating-and-restoring-a-volume-snapshot)
  * [Listing Project IP Addresses](#listing-project-ip-addresses)
  * [Creating a Project for an Organization](#creating-a-project-for-an-organization)
  * [Creating a VLAN](#creating-a-vlan)
* [Contributing](#contributing)
* [Copyright](#copyright)
* [Changes](#changes)

## Installation

The packet python api library can be installed using pip:

    pip install packet-python

Package information available here:

https://pypi.python.org/pypi/packet-python

## Documentation

Full Packet API documenation is available here:
[https://www.packet.net/developers/api/](https://www.packet.net/developers/api/)

## Authentication

Provide your credentials when instantiating client:

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")
```

## Examples

### List Projects

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

projects = manager.list_projects()
for project in projects:
    print(project)
```

### List Plans

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

plans = manager.list_plans()
for plan in plans:
    print(plan)
    if 'cpus' in plan.specs:
        print(plan.specs['cpus'][0]['count'])
```

### Creating a Device

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

device = manager.create_device(project_id='project-id',
                               hostname='node-name-of-your-choice',
                               plan='baremetal_1', facility='ewr1',
                               operating_system='ubuntu_18_04')
print(device)
```

### Checking the Status and Rebooting a Device

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

device = manager.get_device('device-id')
print(device.state)
device.reboot()
```

### Listing all Devices Limiting to 50 per Page

_Packet API defaults to a limit of 10 per page_

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")
params = {
    'per_page': 50
}
devices = manager.list_devices(project_id='project_id', params = params)
print(devices)
```

### Updating a Device

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

device = manager.get_device('device-id')
device.hostname = "test02"
device.description = "new description"

device.update()
```

### Deleting a Device

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

device = manager.get_device('device-id')
device.delete()
```

### Creating a Device Batch

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

batch01 = packet.DeviceBatch({
            "hostname": "batch01",
            "quantity": 2,
            "facility": "ams1",
            "operating_system": "centos_7",
            "plan": "baremetal_0",
        })

device_batch = manager.create_batch(project_id="project_id", params=[batch01])
print(device_batch)
```

### Creating a Volume

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

volume = manager.create_volume(project_id="project-id",
                                description="volume description",
                                plan="storage_1",
                                size="100",
                                facility="ewr1",
                                snapshot_count=7,
                                snapshot_frequency="1day")
print(volume)
```

### Attaching and Detaching a Volume

```python
import packet
import time

manager = packet.Manager(auth_token="yourapiauthtoken")
volume = manager.get_volume("volume_id")

volume.attach("device_id")

while True:
    if manager.get_device("device_id").state == "active":
        break
    time.sleep(2)

volume.detach()
```

## Creating and Restoring a Volume Snapshot

```python
import packet
import time

manager = packet.Manager(auth_token="yourapiauthtoken")

volume = manager.get_volume("volume_id")
volume.create_snapshot()

while True:
    if manager.get_volume(volume.id).state == "active":
        break
    time.sleep(2)

snapshots = manager.get_snapshots(volume.id)
volume.restore(snapshots[0].timestamp)
```

### Listing Project IP Addresses

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

ips = manager.list_project_ips("project_id")
for ip in ips:
    print(ip.address)
```

### Creating a Project for an Organization

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

project = manager.create_organization_project(
    org_id="organization_id",
    name="Integration Tests",
    customdata={"tag": "QA"}
)
print(project)
```

### Creating a VLAN

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

vlan = manager.create_vlan(project_id="project_id", facility="ewr1")
print(vlan)
```

## Contributing

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* You can test your changes with the `test/tests.sh` script, which is what drone uses to check builds.

## Credits

CargoCulted with much gratitude from:
https://github.com/koalalorenzo/python-digitalocean

## Copyright

Copyright (c) 2017 Packet Host. See [License](LICENSE.txt) for further details.

## Changes

See the [Changelog](CHANGELOG.md) for further details.
