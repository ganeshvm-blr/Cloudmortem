import boto3


def discover_ec2():

    client = boto3.client("ec2")

    paginator = client.get_paginator("describe_instances")

    instances = []

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                tags = {tag["Key"]: tag["Value"] for tag in instance.get("Tags", [])}

                instances.append(
                    {
                        "instance_id": instance["InstanceId"],
                        "state": instance["State"]["Name"],
                        "instance_type": instance["InstanceType"],
                        "tags": tags,
                    }
                )

    return instances
