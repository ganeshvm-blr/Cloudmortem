import json
from datetime import datetime, timezone

import boto3


def get_latest_snapshot(bucket_name):

    s3_client = boto3.client("s3")

    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix="inventory/",
    )

    objects = response.get("Contents", [])

    if not objects:
        return None


    latest = sorted(
        objects,
        key=lambda obj: obj["LastModified"],
        reverse=True,
    )[0]


    snapshot = s3_client.get_object(
        Bucket=bucket_name,
        Key=latest["Key"],
    )

    body = snapshot["Body"].read()

    return json.loads(body)


def save_snapshot(inventory, bucket_name):

    s3_client = boto3.client("s3")

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y-%m-%dT%H-%M-%S"
    )

    key = f"inventory/{timestamp}.json"

    s3_client.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(inventory),
        ContentType="application/json",
    )

    return {
        "bucket": bucket_name,
        "key": key,
    }
