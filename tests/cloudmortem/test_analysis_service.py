from platformiq.analysis import SnapshotDiffer
from platformiq.core import Identifier
from platformiq.model import Resource, Snapshot

from cloudmortem.application import AnalysisService


def test_analysis_service_returns_diff_result():
    service = AnalysisService(SnapshotDiffer())

    resource = Resource(
        id=Identifier.new(),
        external_id="resource-001",
    )

    previous = Snapshot(
        id=Identifier.new(),
        resources=(),
    )

    current = Snapshot(
        id=Identifier.new(),
        resources=(resource,),
    )

    result = service.analyze(
        previous,
        current,
    )

    assert result.created == (resource,)
