from __future__ import annotations

from platformiq.model import Snapshot


class InMemorySnapshotStorage:
    """
    Simple snapshot storage for testing
    and local execution.
    """

    def __init__(self):
        self.snapshot = None

    def save(
        self,
        snapshot: Snapshot,
    ) -> None:
        self.snapshot = snapshot

    def load_latest(
        self,
    ) -> Snapshot | None:
        return self.snapshot
