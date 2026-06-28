import boto3


def discover_lambda():

    client = boto3.client("lambda")

    paginator = client.get_paginator(
        "list_functions"
    )

    functions = []

    for page in paginator.paginate():

        for function in page.get("Functions", []):

            functions.append(
                {
                    "name": function["FunctionName"],
                    "runtime": function.get("Runtime"),
                    "last_modified": function["LastModified"],
                }
            )

    return functions
