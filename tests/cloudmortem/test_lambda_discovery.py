from cloudmortem.provider.aws.lambda_function.discovery import LambdaDiscovery
from cloudmortem.provider.aws.lambda_function.mapper import LambdaResourceMapper
from platformiq.model import Resource


class FakeLambdaClient:
    def list_functions(self):
        return {"Functions": [{"FunctionName": "cloudmortem-processor"}]}


def test_lambda_discovery_returns_resources():

    discovery = LambdaDiscovery(
        FakeLambdaClient(),
        LambdaResourceMapper(),
    )

    resources = discovery.discover()

    assert len(resources) == 1
    assert isinstance(resources[0], Resource)
    assert resources[0].external_id == "cloudmortem-processor"
