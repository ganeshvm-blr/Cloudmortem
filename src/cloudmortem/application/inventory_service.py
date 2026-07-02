from __future__ import annotations

from platformiq.contracts import DiscoveryProvider, SnapshotStorage
from platformiq.model import Snapshot


class InventoryService:
    """
    Application service responsible for inventory collection.
    """

    def __init__(
        self,
        discovery_provider: DiscoveryProvider,
        snapshot_storage: SnapshotStorage,
    ):
        self.discovery_provider = discovery_provider
        self.snapshot_storage = snapshot_storage

    def collect_snapshot(self) -> Snapshot:
        """
        Discover and persist the current snapshot.
        """

        snapshot = self.discovery_provider.discover()

        self.snapshot_storage.save(snapshot)

        return snapshot
