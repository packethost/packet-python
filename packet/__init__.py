# -*- coding: utf-8 -*-
"""library to interact with the Packet API"""

__version__ = "1.0"
__author__ = "Aaron Welch ( https://www.packet.net/about/team/aaron-welch/ )"
__author_email__ = "welch@packet.net"
__license__ = "LGPL v3"
__copyright__ = "Copyright (c) 2015, Aaron Welch and Packet"


from .Device import Device  # noqa
from .Facility import Facility  # noqa
from .OperatingSystem import OperatingSystem  # noqa
from .Plan import Plan  # noqa
from .Project import Project  # noqa
from .SSHKey import SSHKey  # noqa
from .Volume import Volume  # noqa
from .Manager import Manager  # noqa
from .baseapi import Error  # noqa
