from cloudmortem.provider.aws import AWSDiscoveryProvider
from platformiq.model import Snapshot


class FakeEC2Discovery:
    def discover(self):
        return ()


class FakeLambdaDiscovery:
    def discover(self):
        return ()


class FakeS3Discovery:
    def discover(self):
        return ()


def test_aws_discovery_provider_returns_snapshot():

    provider = AWSDiscoveryProvider(
        FakeEC2Discovery(),
        FakeLambdaDiscovery(),
        FakeS3Discovery(),
    )

    snapshot = provider.discover()

    assert isinstance(snapshot, Snapshot)
