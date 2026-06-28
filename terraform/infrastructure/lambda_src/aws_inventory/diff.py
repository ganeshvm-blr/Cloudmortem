def compare_resource_lists(
    previous,
    current,
    identifier,
):

    previous_map = {
        item[identifier]: item
        for item in previous
    }

    current_map = {
        item[identifier]: item
        for item in current
    }

    created = [
        current_map[key]
        for key in current_map.keys()
        if key not in previous_map
    ]

    deleted = [
        previous_map[key]
        for key in previous_map.keys()
        if key not in current_map
    ]

    return created, deleted


def compare_snapshots(previous, current):

    changes = {
        "created": [],
        "deleted": [],
        "modified": [],
    }


    # S3 comparison
    s3_created, s3_deleted = compare_resource_lists(
        previous.get("resources", {}).get("s3", []),
        current.get("resources", {}).get("s3", []),
        "name",
    )

    for bucket in s3_created:
        changes["created"].append(
            {
                "service": "s3",
                "resource": bucket["name"],
            }
        )

    for bucket in s3_deleted:
        changes["deleted"].append(
            {
                "service": "s3",
                "resource": bucket["name"],
            }
        )

    # Lambda comparison
    lambda_created, lambda_deleted = compare_resource_lists(
        previous.get("resources", {}).get("lambda", []),
        current.get("resources", {}).get("lambda", []),
        "name",
    )

    for function in lambda_created:
        changes["created"].append(
            {
                "service": "lambda",
                "resource": function["name"],
            }
        )

    for function in lambda_deleted:
        changes["deleted"].append(
            {
                "service": "lambda",
                "resource": function["name"],
            }
        )
    # EC2 comparison
    ec2_created, ec2_deleted = compare_resource_lists(
        previous.get("resources", {}).get("ec2", []),
        current.get("resources", {}).get("ec2", []),
        "instance_id",
    )

    for instance in ec2_created:
        changes["created"].append(
            {
                "service": "ec2",
                "resource": instance["instance_id"],
            }
        )

    for instance in ec2_deleted:
        changes["deleted"].append(
            {
                "service": "ec2",
                "resource": instance["instance_id"],
            }
        )
    return changes
