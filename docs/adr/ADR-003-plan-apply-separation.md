# ADR-003: Separate Terraform Plan and Apply Stages

## Status

Accepted

## Context

Infrastructure changes directly affect production cloud resources.

A deployment workflow that executes `terraform apply` immediately after code changes creates risks:

- Unreviewed infrastructure modifications.
- Accidental resource changes.
- Reduced visibility before production deployment.
- Difficulty auditing what changes were applied.

Production environments require controlled infrastructure change processes where proposed changes can be inspected before execution.

## Decision

CloudMortem separates Terraform execution into distinct plan and apply stages.

The deployment workflow is:

```text
Developer Push
        |
        v
GitHub Actions Validation
        |
        v
Terraform Plan Generation
        |
        v
Terraform Plan Artifact Storage
        |
        v
Production Approval Gate
        |
        v
Terraform Apply Using Approved Plan

The Terraform binary plan generated during validation is stored as an artifact and reused during the deployment stage.

The apply stage does not generate a new plan.

Alternatives Considered
Direct Terraform Apply from CI

Rejected because:
Changes are applied without prior review.
The deployment outcome depends on the current repository state.
Reduces change control visibility.

Manual Terraform Execution from Developer Machines

Rejected because:

Deployment process is inconsistent.
Auditability is reduced.
Environment differences can cause unexpected results.

Consequences

Benefits
Infrastructure changes are reviewable before deployment.
Production deployments follow a controlled workflow.
Deployment history is easier to audit.
Reduces risk of unexpected infrastructure changes.

Trade-offs
Additional pipeline complexity.
Terraform plan artifacts must be managed.
Plans may become invalid if infrastructure changes outside Terraform occur before apply.
Implementation

Implemented in:

.github/workflows/ci.yml

The pipeline:

Generates Terraform plans during validation.
Stores Terraform plan artifacts.
Requires production environment approval.
Applies the previously generated Terraform plan.
