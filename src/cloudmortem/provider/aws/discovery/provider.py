from __future__ import annotations

from platformiq.core import Identifier
from platformiq.model import Snapshot

from ..ec2.discovery import EC2Discovery
from ..lambda_function.discovery import LambdaDiscovery
from ..s3.discovery import S3Discovery


class AWSDiscoveryProvider:
    """
    Coordinates AWS resource discovery across
    supported AWS services.
    """

    def __init__(
        self,
        ec2_discovery: EC2Discovery,
        lambda_discovery: LambdaDiscovery,
        s3_discovery: S3Discovery,
    ):
        self.ec2_discovery = ec2_discovery
        self.lambda_discovery = lambda_discovery
        self.s3_discovery = s3_discovery

    def discover(self) -> Snapshot:
        """
        Discover all supported AWS resources and
        assemble a single snapshot.
        """

        resources = (
            self.ec2_discovery.discover()
            + self.lambda_discovery.discover()
            + self.s3_discovery.discover()
        )

        return Snapshot(
            id=Identifier.new(),
            resources=resources,
        )
