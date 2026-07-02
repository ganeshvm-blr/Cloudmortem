from cloudmortem.storage import S3SnapshotStorage
from platformiq.core import Identifier
from platformiq.model import Snapshot
from platformiq.serialization import SnapshotSerializer


class FakeS3:
    def __init__(self):
        self.data = None

    def put_object(
        self,
        Bucket,
        Key,
        Body,
    ):
        self.data = Body

    def get_object(
        self,
        Bucket,
        Key,
    ):
        return {"Body": FakeBody(self.data)}


class FakeBody:
    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data


def test_s3_storage_saves_snapshot():

    client = FakeS3()

    storage = S3SnapshotStorage(
        client,
        "bucket",
        "snapshot.json",
        SnapshotSerializer(),
    )

    snapshot = Snapshot(id=Identifier.new())

    storage.save(snapshot)

    loaded = storage.load_latest()

    assert loaded["id"] == str(snapshot.id)
