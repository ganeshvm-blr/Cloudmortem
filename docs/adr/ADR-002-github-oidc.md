# ADR-002: Use GitHub Actions OIDC Authentication for AWS Access

## Status

Accepted

## Context

CloudMortem requires GitHub Actions to interact with AWS during infrastructure validation and deployment workflows.

The traditional approach is to store AWS access keys as GitHub repository secrets.

Long-lived AWS credentials create security risks:

- Credentials may be accidentally exposed.
- Rotation becomes an operational burden.
- Access remains valid until manually revoked.
- Secrets provide broader attack opportunities if compromised.

Cloud-native production environments increasingly use short-lived identity federation instead of static credentials.

## Decision

CloudMortem uses GitHub Actions OpenID Connect (OIDC) federation to authenticate with AWS.

The authentication flow is:

```text
GitHub Actions
        |
        v
OIDC Federation
        |
        v
AWS IAM Role
        |
        v
Temporary AWS Credentials
```

GitHub Actions assumes an AWS IAM role using OIDC tokens and receives temporary credentials for the duration of the workflow execution.

No AWS access keys are stored in GitHub.

Alternatives Considered
Static AWS Access Keys

Rejected because:

- Credentials require rotation.
- Secrets can be exposed.
- Access lifecycle management is more difficult.
- Long-lived credentials increase security risk.

Self-Hosted Deployment Credentials

Rejected because:

- Requires additional infrastructure management.
- Introduces credential lifecycle complexity.
- Provides limited advantage for this workload.

Consequences
Benefits
- No long-lived AWS credentials.
- Improved security posture.
- Temporary credential lifecycle.
- Better alignment with AWS security best practices.
- Easier auditing through IAM role assumptions.

Trade-offs
- Requires IAM trust policy configuration.
- Requires understanding OIDC identity federation.
- Initial setup is more complex than static credentials.

Implementation

GitHub Actions workflow:

.github/workflows/ci.yml

AWS authentication uses:

aws-actions/configure-aws-credentials@v4

The workflow assumes an IAM role configured for GitHub OIDC federation.


