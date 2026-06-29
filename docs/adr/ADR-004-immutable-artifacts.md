# ADR-004: Store Immutable Deployment Artifacts

## Status

Accepted

## Context

CloudMortem uses GitHub Actions to validate and deploy infrastructure changes.

A deployment pipeline must ensure that the code and infrastructure artifacts reviewed during validation are the same artifacts used during production deployment.

Rebuilding artifacts during the deployment stage introduces risks:

- The deployed output may differ from the validated output.
- Source changes may occur between validation and deployment.
- Deployment reproducibility is reduced.
- Auditability becomes more difficult.

Production deployment systems commonly promote immutable artifacts through environments rather than rebuilding during each stage.

## Decision

CloudMortem stores deployment artifacts generated during the validation stage and reuses those exact artifacts during deployment.

The pipeline flow is:

```text
Developer Push
        |
        v
GitHub Actions Validation
        |
        +----------------------+
        |                      |
        v                      v
Terraform Plan Artifact   Lambda Package Artifact
        |                      |
        +----------------------+
                       |
                       v
              Production Approval
                       |
                       v
              Terraform Apply

The apply stage consumes:

The previously generated Terraform binary plan.
The previously generated Lambda deployment package.

The deployment workflow does not regenerate these artifacts.

Alternatives Considered
Rebuild Artifacts During Deployment

Rejected because:
Validation and deployment outputs may differ.
Reproducibility is reduced.
Troubleshooting becomes more difficult.

Direct Deployment From Source

Rejected because:

No controlled promotion process exists.
Changes cannot be verified before production execution.
Audit history is limited.

Consequences
Benefits
-Deployments are reproducible.
-Approved artifacts are promoted to production.
-Better supply chain security posture.
-Easier debugging and rollback analysis.

Trade-offs
-Artifact storage lifecycle must be managed.
-Additional CI/CD complexity.
-Old artifacts require cleanup policies.

Implementation
Implemented in:

.github/workflows/ci.yml

The pipeline stores:

Terraform plan artifacts using GitHub Actions artifact storage.
Lambda deployment packages using GitHub Actions artifact storage.

The production apply stage downloads and uses these artifacts.
