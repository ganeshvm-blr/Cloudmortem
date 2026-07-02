from platformiq.core import Identifier
from platformiq.model import Resource, Snapshot


def test_snapshot_has_identifier():
    snapshot = Snapshot(id=Identifier.new())

    assert isinstance(snapshot.id, Identifier)


def test_snapshot_is_empty_by_default():
    snapshot = Snapshot(id=Identifier.new())

    assert snapshot.resources == ()


def test_snapshot_contains_resources():
    resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
    )

    snapshot = Snapshot(
        id=Identifier.new(),
        resources=(resource,),
    )

    assert len(snapshot.resources) == 1
    assert snapshot.resources[0] == resource
