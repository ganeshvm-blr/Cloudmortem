from __future__ import annotations

from platformiq.model import Resource

from .mapper import LambdaResourceMapper


class LambdaDiscovery:
    """
    Discovers AWS Lambda functions.
    """

    def __init__(
        self,
        client,
        mapper: LambdaResourceMapper,
    ):
        self.client = client
        self.mapper = mapper

    def discover(self) -> tuple[Resource, ...]:
        """
        Discover Lambda functions.
        """

        response = self.client.list_functions()

        resources = []

        for function in response.get("Functions", []):
            resources.append(
                self.mapper.map(
                    function_name=function["FunctionName"],
                )
            )

        return tuple(resources)
