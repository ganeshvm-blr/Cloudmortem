variable "project_name" {
  description = "Name of the project"
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
