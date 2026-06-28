resource "aws_iam_role" "lambda_execution_role" {
  name = "${local.name_prefix}-lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [
      {
        Effect = "Allow"

        Principal = {
          Service = "lambda.amazonaws.com"
        }

        Action = "sts:AssumeRole"
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role = aws_iam_role.lambda_execution_role.name

  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
data "aws_iam_policy_document" "inventory_discovery" {
  statement {
    sid    = "InventoryDiscovery"
    effect = "Allow"

    actions = [
      # EC2
      "ec2:DescribeInstances",
      "ec2:DescribeVolumes",
      "ec2:DescribeSnapshots",

      # Lambda
      "lambda:ListFunctions",

      # S3
      "s3:ListAllMyBuckets",
      "s3:GetBucketLocation",
      "s3:GetBucketTagging",
      "s3:GetBucketPolicyStatus",
      "s3:GetBucketAcl",
      "s3:GetBucketVersioning",
      "s3:ListBucket",
      "s3:GetObject",
      "s3:PutObject"
    ]

    resources = ["*"]
  }

  statement {
    sid    = "InventorySnapshotWrite"
    effect = "Allow"

    actions = [
      "s3:PutObject"
    ]

    resources = [
      "${aws_s3_bucket.inventory_snapshots.arn}/inventory/*"
    ]
  }
}
resource "aws_iam_role_policy" "inventory_discovery" {

  name = "cloudmortem-inventory-discovery"

  role = aws_iam_role.lambda_execution_role.id

  policy = data.aws_iam_policy_document.inventory_discovery.json
}

