# -*- coding: utf-8 -*-
"""library to interact with the Packet API"""

__version__ = "1.0"
__author__ = "Aaron Welch ( https://www.packet.net/about/team/aaron-welch/ )"
__author_email__ = "welch@packet.net"
__license__ = "LGPL v3"
__copyright__ = "Copyright (c) 2015, Aaron Welch and Packet"

#from .Device import Device, DeviceError, BadSSHKeyFormat
#from .User import User
#from .Facility import Facility
#from .Plan import Plan
#from .Project import Project
#from .OperatingSystem import OperatingSystem
#from .Action import Action
#from .SSHKey import SSHKey
from .Manager import Manager
from .baseapi import Error
