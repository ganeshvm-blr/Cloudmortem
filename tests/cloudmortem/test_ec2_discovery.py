from cloudmortem.provider.aws.ec2.discovery import EC2Discovery
from cloudmortem.provider.aws.ec2.mapper import EC2ResourceMapper
from platformiq.model import Resource


class FakeEC2Client:
    def describe_instances(self):
        return {"Reservations": [{"Instances": [{"InstanceId": "i-12345"}]}]}


def test_ec2_discovery_returns_resources():

    discovery = EC2Discovery(
        FakeEC2Client(),
        EC2ResourceMapper(),
    )

    resources = discovery.discover()

    assert len(resources) == 1
    assert isinstance(resources[0], Resource)
    assert resources[0].external_id == "i-12345"
