from cloudmortem.storage import FileSnapshotStorage
from platformiq.core import Identifier
from platformiq.model import Snapshot
from platformiq.serialization import SnapshotSerializer


def test_file_storage_saves_snapshot(tmp_path):

    file_path = tmp_path / "snapshot.json"

    storage = FileSnapshotStorage(
        str(file_path),
        SnapshotSerializer(),
    )

    snapshot = Snapshot(id=Identifier.new())

    storage.save(snapshot)

    loaded = storage.load_latest()

    assert loaded["id"] == str(snapshot.id)
