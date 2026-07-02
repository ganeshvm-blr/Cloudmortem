from platformiq.core import Identifier
from platformiq.model import Snapshot

from cloudmortem.application import InventoryService


class FakeDiscoveryProvider:
    def discover(self):
        return Snapshot(id=Identifier.new())


class FakeSnapshotStorage:
    def __init__(self):
        self.saved_snapshot = None

    def save(self, snapshot):
        self.saved_snapshot = snapshot

    def load_latest(self):
        return self.saved_snapshot


def test_inventory_service_collects_and_stores_snapshot():
    discovery = FakeDiscoveryProvider()
    storage = FakeSnapshotStorage()

    service = InventoryService(
        discovery,
        storage,
    )

    snapshot = service.collect_snapshot()

    assert storage.saved_snapshot == snapshot
