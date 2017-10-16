Packet
======

A Python client for the Packet API.

![travis build status badge](https://travis-ci.org/packethost/packet-python.svg?branch=master "Build Status")

Installation
------------
The packet python api library can be installed using pip: `pip install packet-python`

Package information available here:

https://pypi.python.org/pypi/packet-python

Documentation
-------------
Full Packet API documenation is available here:
[https://www.packet.net/developers/api/](https://www.packet.net/developers/api/)

Examples
--------
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
print(device.status)
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
