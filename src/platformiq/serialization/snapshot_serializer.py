from __future__ import annotations

from platformiq.model import Snapshot


class SnapshotSerializer:
    """
    Converts snapshots to and from
    serializable representations.
    """

    def serialize(
        self,
        snapshot: Snapshot,
    ) -> dict:
        return {
            "id": str(snapshot.id),
            "resources": [
                {
                    "id": str(resource.id),
                    "external_id": resource.external_id,
                }
                for resource in snapshot.resources
            ],
        }
