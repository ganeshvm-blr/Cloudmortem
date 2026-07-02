from platformiq.analysis.snapshot_differ import SnapshotDiffer
from platformiq.core import Identifier
from platformiq.model import Resource, Snapshot
from platformiq.model.value_objects import ResourceState


def test_compare_returns_empty_diff_result_for_empty_snapshots():
    differ = SnapshotDiffer()

    previous = Snapshot(id=Identifier.new())
    current = Snapshot(id=Identifier.new())

    result = differ.compare(previous, current)

    assert result.created == ()
    assert result.deleted == ()
    assert result.modified == ()


def test_compare_detects_created_resource():
    differ = SnapshotDiffer()

    resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
    )

    previous = Snapshot(id=Identifier.new())

    current = Snapshot(
        id=Identifier.new(),
        resources=(resource,),
    )

    result = differ.compare(previous, current)

    assert result.created == (resource,)


def test_compare_detects_deleted_resource():
    differ = SnapshotDiffer()

    resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
    )

    previous = Snapshot(
        id=Identifier.new(),
        resources=(resource,),
    )

    current = Snapshot(id=Identifier.new())

    result = differ.compare(previous, current)

    assert result.deleted == (resource,)


def test_compare_detects_modified_resource():
    differ = SnapshotDiffer()

    previous_resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
        state=ResourceState(
            properties={
                "size": "small",
            }
        ),
    )

    current_resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
        state=ResourceState(
            properties={
                "size": "large",
            }
        ),
    )

    previous = Snapshot(
        id=Identifier.new(),
        resources=(previous_resource,),
    )

    current = Snapshot(
        id=Identifier.new(),
        resources=(current_resource,),
    )

    result = differ.compare(previous, current)

    assert result.modified == (current_resource,)
