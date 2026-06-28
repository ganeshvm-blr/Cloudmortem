import json
import logging
import os

from aws_inventory.collector import collect_inventory
from aws_inventory.snapshot import (
    save_snapshot,
    get_latest_snapshot,
)
from aws_inventory.diff import compare_snapshots


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logger.info("CloudMortem event received")

    logger.info(json.dumps(event))

    bucket_name = os.environ["SNAPSHOT_BUCKET"]

    previous_inventory = get_latest_snapshot(
        bucket_name
    )

    current_inventory = collect_inventory()

    changes = {
        "created": [],
        "deleted": [],
        "modified": [],
    }

    if previous_inventory:

        changes = compare_snapshots(
            previous_inventory,
            current_inventory,
        )

    snapshot = save_snapshot(
        current_inventory,
        bucket_name,
    )

    current_inventory["snapshot"] = snapshot

    current_inventory["changes"] = changes

    logger.info(
        json.dumps(current_inventory)
    )

    return {
        "statusCode": 200,
        "body": json.dumps(current_inventory)
    }
