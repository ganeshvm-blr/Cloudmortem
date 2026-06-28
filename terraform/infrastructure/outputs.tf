output "terraform_plan_role_arn" {
  description = "ARN of the GitHub Actions Terraform plan role"
  value       = aws_iam_role.terraform_plan_role.arn
}
