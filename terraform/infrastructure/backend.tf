terraform {
  backend "s3" {
    bucket       = "cloudmortem-716215155311-dev-state"
    key          = "infrastructure/terraform.tfstate"
    region       = "ap-south-1"
    use_lockfile = true
  }
}
