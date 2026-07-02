from __future__ import annotations

import json

from platformiq.model import Snapshot
from platformiq.serialization import SnapshotSerializer


class S3SnapshotStorage:
    """
    Stores snapshots in Amazon S3.
    """

    def __init__(
        self,
        client,
        bucket: str,
        key: str,
        serializer: SnapshotSerializer,
    ):
        self.client = client
        self.bucket = bucket
        self.key = key
        self.serializer = serializer

    def save(
        self,
        snapshot: Snapshot,
    ) -> None:

        data = self.serializer.serialize(snapshot)

        self.client.put_object(
            Bucket=self.bucket,
            Key=self.key,
            Body=json.dumps(data),
        )

    def load_latest(self) -> dict | None:

        response = self.client.get_object(
            Bucket=self.bucket,
            Key=self.key,
        )

        return json.loads(response["Body"].read())
