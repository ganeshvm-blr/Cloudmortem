resource "aws_s3_bucket" "inventory_snapshots" {

  bucket = "${local.name_prefix}-snapshots"

  tags = {
    Name = "${local.name_prefix}-snapshots"
  }
}
