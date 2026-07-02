from cloudmortem import InventoryService
from cloudmortem.provider.aws import AWSDiscoveryProvider
from cloudmortem.storage import InMemorySnapshotStorage
from platformiq.model import Snapshot


class FakeEC2Discovery:
    def discover(self):
        return ()


class FakeLambdaDiscovery:
    def discover(self):
        return ()


class FakeS3Discovery:
    def discover(self):
        return ()


def test_aws_inventory_workflow():

    provider = AWSDiscoveryProvider(
        FakeEC2Discovery(),
        FakeLambdaDiscovery(),
        FakeS3Discovery(),
    )

    storage = InMemorySnapshotStorage()

    service = InventoryService(
        provider,
        storage,
    )

    snapshot = service.collect_snapshot()

    assert isinstance(snapshot, Snapshot)
    assert storage.load_latest() == snapshot
