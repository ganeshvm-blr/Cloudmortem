import boto3
import logging

from aws_inventory.ec2 import discover_ec2
from aws_inventory.lambda_service import discover_lambda
from aws_inventory.s3 import discover_s3
from aws_inventory.schema import build_inventory


logger = logging.getLogger()


def safe_discover(service_name, function):

    try:
        return function(), None

    except Exception as error:

        logger.exception(
            "%s discovery failed",
            service_name
        )

        return [], {
            "service": service_name,
            "error": str(error),
        }


def collect_inventory():

    region = boto3.Session().region_name

    ec2, ec2_error = safe_discover(
        "ec2",
        discover_ec2
    )

    lambdas, lambda_error = safe_discover(
        "lambda",
        discover_lambda
    )

    s3, s3_error = safe_discover(
        "s3",
        discover_s3
    )

    inventory = build_inventory(
        ec2,
        lambdas,
        s3,
        region,
    )

    errors = [
        error
        for error in [
            ec2_error,
            lambda_error,
            s3_error,
        ]
        if error
    ]

    if errors:
        inventory["errors"] = errors

    return inventory
