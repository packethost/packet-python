# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

"""library to interact with the Packet API"""

__version__ = "1.38.2"
__author__ = "Packet Engineers"
__author_email__ = "help@packet.net"
__license__ = "LGPL v3"
__copyright__ = "Copyright (c) 2019, Packet"

from .Device import Device  # noqa
from .Facility import Facility  # noqa
from .OperatingSystem import OperatingSystem  # noqa
from .Plan import Plan  # noqa
from .Project import Project  # noqa
from .SSHKey import SSHKey  # noqa
from .Volume import Volume  # noqa
from .Manager import Manager  # noqa
from .baseapi import Error  # noqa
from .MetadataList import MetadataList # noqa
