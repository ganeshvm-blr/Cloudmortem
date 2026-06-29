# ADR-006: Deployment Concurrency Protection

## Status

Accepted

## Context

CloudMortem uses GitHub Actions to automate infrastructure validation and deployment.

Production infrastructure changes must be executed in a controlled manner.

Without deployment concurrency controls, multiple workflow executions can attempt infrastructure changes at the same time.

This creates risks:

- Conflicting Terraform operations.
- Race conditions between deployments.
- Unexpected infrastructure state changes.
- Reduced deployment reliability.

Infrastructure deployment systems commonly use locking mechanisms to ensure only one production change executes at a time.

## Decision

CloudMortem uses GitHub Actions concurrency controls to prevent overlapping production deployments.

The workflow configuration:

```yaml
concurrency:
  group: cloudmortem-production
  cancel-in-progress: false

ensures that:

Only one production deployment workflow runs at a time.
New deployments wait for the current deployment to complete.
Active infrastructure changes are not cancelled unexpectedly.

Alternatives Considered

Allow Concurrent Deployments
Rejected because:
Multiple Terraform operations can conflict.
Deployment ordering becomes unpredictable.
Production state consistency is harder to maintain.

Cancel Previous Deployments Automatically
Rejected because:
An active infrastructure change should complete safely.
Cancelling Terraform operations may leave uncertainty about applied changes.

Consequences

Benefits
Prevents overlapping production deployments.
Improves infrastructure state consistency.
Reduces deployment race conditions.
Provides safer CI/CD execution.

Trade-offs
Deployment queue time may increase during frequent changes.
Requires workflow configuration management.

Implementation

Implemented in:

.github/workflows/ci.yml

Configuration:

concurrency:
  group: cloudmortem-production
  cancel-in-progress: false

The concurrency group applies deployment serialization for production workflows.
