from __future__ import annotations

from platformiq.model import Resource

from .mapper import EC2ResourceMapper


class EC2Discovery:
    """
    Discovers AWS EC2 instances.
    """

    def __init__(
        self,
        client,
        mapper: EC2ResourceMapper,
    ):
        self.client = client
        self.mapper = mapper

    def discover(self) -> tuple[Resource, ...]:
        """
        Discover EC2 instances.
        """

        response = self.client.describe_instances()

        resources = []

        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                resources.append(
                    self.mapper.map(
                        instance_id=instance["InstanceId"],
                    )
                )

        return tuple(resources)
