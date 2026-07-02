from cloudmortem.provider.aws.ec2.mapper import EC2ResourceMapper
from platformiq.model import Resource


def test_ec2_resource_mapper_creates_resource():
    mapper = EC2ResourceMapper()

    resource = mapper.map(
        instance_id="i-123456",
    )

    assert isinstance(resource, Resource)
    assert resource.external_id == "i-123456"
