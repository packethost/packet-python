Packet
======

A Python client for the Packet API.

![travis build status badge](https://travis-ci.org/packethost/packet-python.svg?branch=master "Build Status")

Installation
------------
The packet python api library can be installed using pip:

    pip install packet-python

Package information available here:

https://pypi.python.org/pypi/packet-python

Documentation
-------------
Full Packet API documenation is available here:
[https://www.packet.net/developers/api/](https://www.packet.net/developers/api/)

Examples
--------

# Authentication

Provide your credentials when instantiating client:

```python
import packet

self.manager = packet.Manager(auth_token="yourapiauthtoken")
```

# Operations

## Servers

## Create a server

Creates a new server and provisions it in our datacenter.

```
self.device = self.manager.create_device(
            "project_id", "devicetest", "baremetal_0", "ewr1", "centos_7"
        )
```

Available parameters

| NAME| TYPE | DESCRIPTION | REQUIRED |
|---|---|---|---|
| project_id | string | 	Project UUID  under which server will be created| Yes |
| hostname | string | The hostname of the server. | Yes |
| plan | string | Plan name| Yes |
| facility | string | Facility code | Yes |
| operating_system | string || Yes |
| description | string | | No |
| billing_cycle | string | | No |
| always_pxe | string | | No |
| ipxe_script_url | string | | No |
| userdata | string | | No |
| locked | string | | No |
| hardware_reservation_id | string | | No |
| spot_instance | string | | No |
| spot_price_max | string | | No |
| termination_time | string | | No |
| tags | string | | No |
| project_ssh_keys | collection of strings | | No |
| user_ssh_keys | collection of strings | | No |
| features | string | | No |

## Retrieve a server

Gets details about a specified server

```python
response = compute.servers.get(server_id)
```

## Update a server
Updates a server
```python
self.device.hostname= 'test02'

self.device = self.device.update
```

Available parameters

| NAME| TYPE | DESCRIPTION | REQUIRED |
|---|---|---|---|
| hostname | string | The hostname of the server. | No |
| description | string | | No |
| billing_cycle | string | | No |
| always_pxe | string | | No |
| ipxe_script_url | string | | No |
| userdata | string | | No |
| locked | string | | No |
| spot_instance | string | | No |

## Reboot a server
Reboots the specified server

```python
self.device.reboot
```

## Power off server
Powers off the specified server

```python
self.device.power_off
```

## Power on server
Powers on the specified server

```python
self.device.power_on
```

## Delete a server

Deletes the specified servers

```python
self.device.delete
```

## Volumes

## Create a volume
Creates a new volume

```python
self.volume = self.manager.create_volume("project_id,
                                                "volume description",
                                                "storage_1",
                                                "100",
                                                "ewr1",
                                                7,
                                                "1day")
```


Available parameters

| NAME| TYPE | DESCRIPTION | REQUIRED |
|---|---|---|---|
| facility | string | Facility code | Yes |
| plan | string | Plan name| Yes |
| size | int | Volume size| Yes |
| description | string | | Yes |
| snapshot_count | string | | No |
| snapshot_frequency | string | | No |


## Retrieve a volume

Gets a specified volume

```python
self.volume = self.manager.get_volume("volume_id)
```

## List volumes
List all volumes in the specified project

```python
volumes = self.manager.list_volumes("project_id")
```

Optional parameters 

| NAME| TYPE | DESCRIPTION | 
|---|---|---|
| without_projects | string | | 
| per_page | string | | 
| page | string | | 
| include | string | For resources that contain collections of other resources, the Packet API will return links to the other resources by default. | 

## Attach a volume

Attaches a volume to the specified server

```python
self.volume.attach("device_id")
```

## Detach a volume

Detaches a volume from the specified server

```python
self.volume.detach("device_id")
```

## Delete a volume
Deletes a specified volume

```python
self.volume.delete
```

### List projects

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

projects = manager.list_projects()
for project in projects:
    print(project)
```


### List plans

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
                               operating_system='ubuntu_14_04')
print(device)
```

### Checking the status and rebooting a Device

```python
import packet
manager = packet.Manager(auth_token="yourapiauthtoken")

device = manager.get_device('device-id')
print(device.state)
device.reboot()
```

### Listing all devices, limiting to 50 per page

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

Contributing
------------

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* You can test your changes with the `test/tests.sh` script, which is what travis uses to check builds.

Credits
-------

CargoCulted with much gratitude from:
https://github.com/koalalorenzo/python-digitalocean

Copyright
---------

Copyright (c) 2017 Packet Host. See [License](LICENSE.txt) for further details.

Changes
-------

See the [Changelog](CHANGELOG.md) for further details.
