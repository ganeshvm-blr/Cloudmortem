from cloudmortem.provider.aws.s3.discovery import S3Discovery
from cloudmortem.provider.aws.s3.mapper import S3ResourceMapper
from platformiq.model import Resource


class FakeS3Client:
    def list_buckets(self):
        return {"Buckets": [{"Name": "cloudmortem-state"}]}


def test_s3_discovery_returns_resources():

    discovery = S3Discovery(
        FakeS3Client(),
        S3ResourceMapper(),
    )

    resources = discovery.discover()

    assert len(resources) == 1
    assert isinstance(resources[0], Resource)
    assert resources[0].external_id == "cloudmortem-state"
