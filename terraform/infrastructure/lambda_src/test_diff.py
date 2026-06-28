from aws_inventory.diff import compare_snapshots


old = {
    "resources": {
        "s3": [
            {"name": "old-bucket"}
        ],
        "lambda": [],
        "ec2": []
    }
}


new = {
    "resources": {
        "s3": [
            {"name": "old-bucket"},
            {"name": "new-bucket"}
        ],
        "lambda": [],
        "ec2": []
    }
}


result = compare_snapshots(old, new)

print(result)
