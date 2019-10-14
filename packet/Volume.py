# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

from .Plan import Plan
from .Facility import Facility


class Volume:
    def __init__(self, data, manager):
        self.manager = manager
        if data is None:
            return

        self.id = data.get("id")
        self.name = data.get("name")
        self.description = data.get("description")
        self.size = data.get("size")
        self.state = data.get("state")
        self.locked = data.get("locked")
        self.billing_cycle = data.get("billing_cycle")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.attachments = data.get("attachments")

        self.plan = Plan(data.get("plan"))
        self.facility = Facility(data.get("facility"))
        try:
            self.attached_to = data["attachments"][0]["device"]["id"]
        except (KeyError, IndexError):
            self.attached_to = None

    def update(self):
        params = {
            "description": self.description,
            "size": self.size,
            "plan": self.plan.slug,
            "locked": self.locked,
        }

        return self.manager.call_api(
            "storage/%s" % self.id, type="PATCH", params=params
        )

    def delete(self):
        return self.manager.call_api("storage/%s" % self.id, type="DELETE")

    def attach(self, device_id):
        params = {"device_id": device_id}
        return self.manager.call_api(
            "storage/%s/attachments" % self.id, type="POST", params=params
        )

    def detach(self):
        for attachment in self.attachments:
            return self.manager.call_api(attachment["href"], type="DELETE")

    def list_snapshots(self, params={}):
        data = self.manager.call_api("storage/%s/snapshots" % (self.id))
        snapshots = list()
        for jsoned in data["snapshots"]:
            snapshot = VolumeSnapshot(jsoned, self)
            snapshots.append(snapshot)
        return snapshots

    def create_snapshot(self):
        self.manager.call_api("storage/%s/snapshots" % self.id, type="POST")

    def create_snapshot_policy(self, frequency, count):
        """Creates a new snapshot policy of your volume.

        :param frequency:  (required) Snapshot frequency

        Validation of `frequency` is left to the packet api to avoid going out
        of date if any new value is introduced.
        The currently known values are:
          - 1hour,
          - 1day
          - 1week
          - 1month
          - 1year
        """
        data = self.manager.call_api(
            "storage/{0}/snapshot-policies?snapshot_frequency={1}&snapshot_count={2}".format(
                self.id, frequency, count
            ),
            type="POST",
        )
        return SnapshotPolicy(data, self)

    def clone(self):
        return Volume(
            self.manager.call_api("storage/%s/clone" % self.id, type="POST"),
            manager=self.manager,
        )

    def restore(self, restore_point):
        self.manager.restore_volume(self.id, restore_point=restore_point)

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)


class VolumeSnapshot:
    def __init__(self, data, volume):
        self.volume = volume

        self.id = data["id"]
        self.status = data["status"]
        self.timestamp = data["timestamp"]
        self.created_at = data["created_at"]

    def delete(self):
        return self.volume.manager.call_api(
            "/storage/%s/snapshots/%s" % (self.volume.id, self.id), type="DELETE"
        )

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)


class SnapshotPolicy:
    def __init__(self, data, policy):
        self.policy = policy

        self.id = data["id"]
        self.count = data["snapshot_count"]
        self.frequency = data["snapshot_frequency"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def delete(self):
        return self.policy.manager.call_api(
            "storage/snapshot-policies/%s" % self.id, type="DELETE"
        )

    def update_snapshot_policy(self, frequency, count):
        """Updates the volume snapshot policy.

           :param frequency:  (required) Snapshot frequency

           Validation of `frequency` is left to the packet api to avoid going out
           of date if any new value is introduced.
           The currently known values are:
             - 1hour,
             - 1day
             - 1week
             - 1month
             - 1year
       """
        data = self.policy.manager.call_api(
            "storage/snapshot-policies/{0}?snapshot_frequency={1}&snapshot_count={2}".format(
                self.id, frequency, count
            ),
            type="PATCH",
        )
        return SnapshotPolicy(data, self)

    def __str__(self):
        return "%s" % self.id

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.id)
