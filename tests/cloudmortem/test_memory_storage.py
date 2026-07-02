from cloudmortem.storage import InMemorySnapshotStorage
from platformiq.core import Identifier
from platformiq.model import Snapshot


def test_memory_storage_saves_and_loads_snapshot():

    storage = InMemorySnapshotStorage()

    snapshot = Snapshot(id=Identifier.new())

    storage.save(snapshot)

    assert storage.load_latest() == snapshot
