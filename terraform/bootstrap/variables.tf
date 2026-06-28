variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "cloudmortem"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "ap-south-1"
}
