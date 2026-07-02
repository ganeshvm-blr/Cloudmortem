from platformiq.contracts import DiscoveryProvider
from platformiq.core import Identifier
from platformiq.model import Snapshot


class FakeDiscoveryProvider(DiscoveryProvider):
    def discover(self) -> Snapshot:
        return Snapshot(id=Identifier.new())


def test_discovery_provider_returns_snapshot():
    provider = FakeDiscoveryProvider()

    snapshot = provider.discover()

    assert isinstance(snapshot, Snapshot)
