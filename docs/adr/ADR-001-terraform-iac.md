# ADR-001: Use Terraform for Infrastructure Management

## Status

Accepted

## Context

CloudMortem requires repeatable, version-controlled management of AWS infrastructure.

Managing infrastructure manually through the AWS Console introduces risks:

- Configuration drift between environments.
- Manual deployment errors.
- Difficulty reviewing infrastructure changes.
- Lack of audit history.

Alternative infrastructure management tools were considered, including AWS CloudFormation and manual provisioning.

## Decision

CloudMortem uses Terraform as the Infrastructure as Code (IaC) tool for managing AWS resources.

Terraform manages:

- AWS Lambda functions.
- IAM roles and policies.
- EventBridge scheduling.
- Amazon S3 resources.
- CloudWatch resources.

Infrastructure changes are reviewed through Git version control and validated through GitHub Actions before deployment.

## Alternatives Considered

### AWS CloudFormation

Rejected because Terraform provides:

- Multi-cloud portability.
- A large ecosystem.
- Strong community adoption.
- A declarative configuration model familiar across DevOps environments.

### Manual AWS Console Provisioning

Rejected because it does not provide:

- Repeatability.
- Version control.
- Automated validation.
- Reliable environment recreation.

## Consequences

### Benefits

- Infrastructure is version controlled.
- Deployments are repeatable.
- Changes can be reviewed before production.
- CI/CD automation becomes possible.

### Trade-offs

- Terraform state management becomes an operational responsibility.
- Engineers must understand Terraform lifecycle behavior.
- Additional tooling is required in the deployment pipeline.

## Implementation

Terraform configuration is located at:
terraform/
├── bootstrap/
└── infrastructure/

Deployment is automated through GitHub Actions.
