resource "aws_cloudwatch_event_rule" "cloudmortem_schedule" {
  name = "${local.name_prefix}-event-rule"

  description = "Triggers CloudMortem processing workflow"

  schedule_expression = "rate(5 minutes)"
}
resource "aws_cloudwatch_event_target" "cloudmortem_lambda_target" {
  rule = aws_cloudwatch_event_rule.cloudmortem_schedule.name

  target_id = "CloudMortemLambdaTarget"

  arn = aws_lambda_function.cloudmortem_processor.arn
}


resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id = "AllowExecutionFromEventBridge"

  action = "lambda:InvokeFunction"

  function_name = aws_lambda_function.cloudmortem_processor.function_name

  principal = "events.amazonaws.com"

  source_arn = aws_cloudwatch_event_rule.cloudmortem_schedule.arn
}
