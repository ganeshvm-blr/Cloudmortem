import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parents[1]
        / "terraform"
        / "infrastructure"
        / "lambda_src"
    )
)

from aws_inventory.diff import compare_snapshots


def test_detect_created_resource():
    old = {"resources": {"s3": [{"name": "old-bucket"}], "lambda": [], "ec2": []}}

    new = {
        "resources": {
            "s3": [{"name": "old-bucket"}, {"name": "new-bucket"}],
            "lambda": [],
            "ec2": [],
        }
    }

    result = compare_snapshots(old, new)

    assert result["created"] == [{"service": "s3", "resource": "new-bucket"}]

    assert result["deleted"] == []
    assert result["modified"] == []


def test_detect_deleted_resource():
    old = {"resources": {"s3": [{"name": "deleted-bucket"}], "lambda": [], "ec2": []}}

    new = {"resources": {"s3": [], "lambda": [], "ec2": []}}

    result = compare_snapshots(old, new)

    assert result["deleted"] == [{"service": "s3", "resource": "deleted-bucket"}]

    assert result["created"] == []
    assert result["modified"] == []
