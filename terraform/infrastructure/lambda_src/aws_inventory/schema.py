from datetime import datetime, timezone


def build_inventory(ec2, lambdas, s3, region):

    return {
        "metadata": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "region": region,
        },
        "summary": {
            "ec2_count": len(ec2),
            "lambda_count": len(lambdas),
            "s3_count": len(s3),
            "total_resources": (
                len(ec2)
                + len(lambdas)
                + len(s3)
            ),
        },
        "resources": {
            "ec2": ec2,
            "lambda": lambdas,
            "s3": s3,
        },
    }
