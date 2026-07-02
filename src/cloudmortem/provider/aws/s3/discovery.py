from __future__ import annotations

from platformiq.model import Resource

from .mapper import S3ResourceMapper


class S3Discovery:
    """
    Discovers AWS S3 buckets.
    """

    def __init__(
        self,
        client,
        mapper: S3ResourceMapper,
    ):
        self.client = client
        self.mapper = mapper

    def discover(self) -> tuple[Resource, ...]:
        """
        Discover S3 buckets.
        """

        response = self.client.list_buckets()

        resources = []

        for bucket in response.get("Buckets", []):
            resources.append(
                self.mapper.map(
                    bucket_name=bucket["Name"],
                )
            )

        return tuple(resources)
