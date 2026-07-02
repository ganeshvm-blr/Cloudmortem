from __future__ import annotations

import json
from pathlib import Path

from platformiq.model import Snapshot
from platformiq.serialization import SnapshotSerializer


class FileSnapshotStorage:
    """
    Stores snapshots on local filesystem.
    """

    def __init__(
        self,
        path: str,
        serializer: SnapshotSerializer,
    ):
        self.path = Path(path)
        self.serializer = serializer

    def save(
        self,
        snapshot: Snapshot,
    ) -> None:

        data = self.serializer.serialize(snapshot)

        self.path.write_text(json.dumps(data))

    def load_latest(self) -> dict | None:

        if not self.path.exists():
            return None

        return json.loads(self.path.read_text())
