#packet-python
##

This library provides easy access to Packet's API


## Features
packet-python supports all the features provided via the Packet API, such as:

* Manage Projects
* Manage a Project's Users and Devices
* Manage SSH Keys
* Power Off, Power On and Reboot Devices

## Examples
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

device = manager.create_device(project='project-id',
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

## Testing

Yes.

## Links

  * GitHub: [https://github.com/packethost/packet-python](https://github.com/packethost/packet-python)
  * Author Website: [https://www.packet.net/team/aaron-welch](https://www.packet.net/team/aaron-welch)

## Credits

CargoCulted with much gratitude from:
https://github.com/koalalorenzo/python-digitalocean
