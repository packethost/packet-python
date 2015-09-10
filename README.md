Packet
======

A Python client for the Packet API.

Documentation
-------------
Full Packet API documenation is available here:
[https://www.packet.net/dev/api/](https://www.packet.net/dev/api/)

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

Testing
-------

Yes.

Contributing
------------

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* Make sure to add tests for it. This is important so we don't break it in a future version unintentionally.

Credits
-------

CargoCulted with much gratitude from:
https://github.com/koalalorenzo/python-digitalocean

Copyright
---------

Copyright (c) 2015 Packet Host. See `LICENSE.txt` for further details.
