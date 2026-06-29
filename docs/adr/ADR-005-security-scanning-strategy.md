# ADR-005: Infrastructure Security Scanning Strategy

## Status

Accepted

## Context

CloudMortem infrastructure is managed using Terraform.

Infrastructure as Code introduces the ability to review and automate changes, but it can also introduce security risks through incorrect configurations.

Examples include:

- Overly permissive IAM policies.
- Publicly exposed resources.
- Missing security controls.
- Infrastructure configuration drift from security expectations.

Security validation should occur before infrastructure changes reach deployment stages.

## Decision

CloudMortem performs automated Terraform security scanning during the GitHub Actions validation workflow.

The pipeline uses Checkov to analyze Terraform configurations for security and compliance issues.

The validation workflow includes:

```text
Developer Push
        |
        v
GitHub Actions
        |
        +----------------+
        |                |
        v                v
Terraform Validation   Checkov Security Scan
        |
        v
Terraform Plan

Security scanning occurs before Terraform planning and deployment artifacts are generated.

Alternatives Considered

Manual Security Reviews

Rejected because:

Security checks are inconsistent.
Issues may be discovered late.
Manual reviews do not scale with frequent deployments.

Security Scanning After Deployment

Rejected because:

Misconfigurations reach cloud environments first.
Remediation becomes reactive.
Deployment risk increases.

Consequences

Benefits
Security issues are identified earlier.
Infrastructure changes receive automated validation.
Security becomes part of the delivery lifecycle.
Improves cloud deployment maturity.

Trade-offs
Security tools require maintenance and updates.
False positives may require investigation.
Additional CI execution time is introduced.

Implementation

Implemented in:

.github/workflows/ci.yml

The workflow installs and executes Checkov:

pip install checkov

checkov -d terraform --soft-fail

The scan currently uses soft-fail mode to provide visibility while allowing continued development.

Future improvements may introduce enforcement policies for production-critical findings.
