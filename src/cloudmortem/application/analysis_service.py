from __future__ import annotations

from platformiq.analysis.snapshot_differ import SnapshotDiffer
from platformiq.model import DiffResult, Snapshot


class AnalysisService:
    """
    Application service responsible for
    infrastructure drift analysis.
    """

    def __init__(self, snapshot_differ: SnapshotDiffer):
        self.snapshot_differ = snapshot_differ

    def analyze(
        self,
        previous: Snapshot,
        current: Snapshot,
    ) -> DiffResult:
        """
        Compare two snapshots and return drift results.
        """

        return self.snapshot_differ.compare(
            previous,
            current,
        )
