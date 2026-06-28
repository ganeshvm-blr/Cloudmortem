data "archive_file" "lambda_package" {
  type        = "zip"
  source_dir  = "${path.module}/lambda_src"
  output_path = "${path.module}/lambda_function.zip"
}


resource "aws_lambda_function" "cloudmortem_processor" {
  function_name = "${local.name_prefix}-processor"

  filename = data.archive_file.lambda_package.output_path

  source_code_hash = data.archive_file.lambda_package.output_base64sha256

  role = aws_iam_role.lambda_execution_role.arn

  handler = "lambda_function.lambda_handler"

  runtime = "python3.12"

  timeout = 30
  environment {
    variables = {
      SNAPSHOT_BUCKET = aws_s3_bucket.inventory_snapshots.bucket
    }
  }
  depends_on = [
    aws_cloudwatch_log_group.lambda_logs
  ]
}
