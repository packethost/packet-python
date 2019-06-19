# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only


class MetadataList(list):
    def __init__(self, data, metadata):
        list.__init__(self, data)
        self.meta = metadata
