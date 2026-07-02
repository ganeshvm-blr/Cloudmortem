from __future__ import annotations

from platformiq.model import Snapshot


class AWSDiscoveryProvider:
    """
    Coordinates AWS resource discovery.

    Individual AWS service discovery implementations
    will be added separately.
    """

    def discover(self) -> Snapshot:
        """
        Discover AWS resources.
        """

        raise NotImplementedError("AWS discovery is not implemented yet")
