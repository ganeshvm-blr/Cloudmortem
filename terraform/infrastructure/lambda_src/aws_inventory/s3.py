import boto3


def discover_s3():

    client = boto3.client("s3")

    response = client.list_buckets()

    buckets = []

    for bucket in response.get("Buckets", []):

        name = bucket["Name"]

        try:

            location = client.get_bucket_location(
                Bucket=name
            )

            region = (
                location.get("LocationConstraint")
                or "us-east-1"
            )

        except Exception:

            region = "unknown"

        buckets.append(
            {
                "name": name,
                "region": region,
                "creation_date": bucket["CreationDate"].isoformat(),
            }
        )

    return buckets
