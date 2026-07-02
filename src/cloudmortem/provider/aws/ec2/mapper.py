from __future__ import annotations

from platformiq.core import Identifier
from platformiq.model import Resource


class EC2ResourceMapper:
    """
    Converts AWS EC2 instance representations
    into PlatformIQ resources.
    """

    def map(
        self,
        instance_id: str,
    ) -> Resource:
        return Resource(
            id=Identifier.new(),
            external_id=instance_id,
        )
