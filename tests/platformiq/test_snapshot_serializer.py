from platformiq.core import Identifier
from platformiq.model import Snapshot
from platformiq.serialization import SnapshotSerializer


def test_snapshot_serializer_creates_dict():

    snapshot = Snapshot(id=Identifier.new())

    serializer = SnapshotSerializer()

    result = serializer.serialize(snapshot)

    assert "id" in result
    assert "resources" in result
