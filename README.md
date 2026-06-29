# CloudMortem

Serverless AWS infrastructure inventory and drift detection platform.

## Problem Statement

Cloud infrastructure changes continuously through deployments, manual modifications,
and configuration updates. Without visibility into these changes, teams can lose
track of the actual state of their AWS environment.

CloudMortem provides automated infrastructure inventory collection and drift detection
by comparing current AWS resources against previously stored snapshots.

## Overview

CloudMortem automatically discovers AWS resources, stores inventory snapshots,
and detects infrastructure drift between current AWS state and historical state.
## Current Features

- AWS resource discovery
- Lambda based processing
- Terraform infrastructure deployment
- S3 inventory snapshot storage
- Snapshot comparison engine
- Drift detection reporting

## Architecture

CloudMortem uses a serverless event-driven architecture.

                EventBridge Scheduler
                        |
                        v
          cloudmortem-dev-processor Lambda
                        |
      +-----------------+-----------------+
      |                 |                 |
      v                 v                 v
    EC2              Lambda              S3
Describe APIs    ListFunctions      ListBuckets
      |                 |                 |
      +-----------------+-----------------+
                        |
                        v
              Inventory Snapshot
                        |
                        v
          S3 Snapshot Storage Bucket
                        |
                        v
               Drift Comparison Engine
                        |
                        v
          Created / Deleted / Modified Resources


Deployment Architecture Diagram

                GitHub Repository
                       |
                       v
              GitHub Actions Pipeline
                       |
        +--------------+--------------+
        |                             |
 Terraform Validation          Python Tests
        |
        v
 Terraform Plan
        |
        v
 Artifact Storage
        |
        |
 Production Approval
        |
        v
 Terraform Apply
        |
        v
 AWS Infrastructure

Deployment workflow:

Code changes trigger GitHub Actions.
Terraform validates infrastructure configuration.
Terraform creates an execution plan that is reviewed before deployment.
The Terraform plan and Lambda package are stored as immutable artifacts.
A production environment approval gate requires manual review.
Terraform applies the exact previously reviewed binary plan artifact.

This ensures production deployments use reviewed infrastructure changes rather than directly applying unverified configuration.

Secure Deployment Authentication

CloudMortem uses GitHub Actions OpenID Connect (OIDC) authentication instead of long-lived AWS credentials.

Benefits:

No AWS access keys stored in GitHub.
Short-lived IAM credentials.
Improved security posture.
Better alignment with production cloud deployment practices.


## Example Drift Detection Output

CloudMortem identifies infrastructure changes by comparing inventory snapshots.

Example: A new S3 bucket was created outside the expected infrastructure workflow.

Detected change:

```json
{
  "changes": {
    "created": [
      {
        "service": "s3",
        "resource": "cloudmortem-drift-test-716215155311"
      }
    ],
    "deleted": [],
    "modified": []
  }
}
```

The detection confirms that CloudMortem can identify resources that appear in the AWS environment after the previous inventory snapshot was captured.


## Tech Stack

- AWS Lambda
- Amazon S3
- Terraform
- Python
- IAM
- EventBridge

## CI/CD Workflow

CloudMortem uses GitHub Actions to implement a controlled infrastructure deployment workflow.

The pipeline separates validation, planning, approval, and deployment stages.

Current pipeline:

Developer
|
|
Git Push
|
|
GitHub Actions
|
+-- Python validation
|
+-- Python tests
|
+-- Terraform formatting check
|
+-- Terraform validation
|
+-- Terraform plan generation
|
+-- Terraform plan artifact storage
|
+-- Lambda deployment package artifact storage
|
|
Production Approval Gate
|
|
Terraform Apply


---

# 2. Add Security Model Section

After Tech Stack, add:

```markdown
## Security Model

CloudMortem follows several cloud security principles.

### GitHub Actions OIDC Authentication

GitHub Actions authenticates with AWS through OpenID Connect federation.

The workflow assumes an AWS IAM role using temporary credentials instead of storing permanent AWS access keys.

### IAM Least Privilege

AWS permissions are separated by workload.

Lambda uses an execution role with permissions required for inventory collection.

Terraform deployment uses a separate IAM role assumed by GitHub Actions.

### Infrastructure Change Control

Production infrastructure changes require:

- Terraform plan generation
- Artifact review
- Manual approval
- Controlled Terraform apply

## Repository Structure

```text
CloudMortem/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── COST_ANALYSIS.md
│   ├── DECISIONS.md
│   ├── FAILURE_SCENARIOS.md
│   ├── INTERVIEW_NOTES.md
│   └── LESSONS_LEARNED.md
│
├── scripts/
│   └── Utility scripts
│
├── src/
│   └── Reserved for future application source separation
│
├── tests/
│   └── test_diff.py
│
└── terraform/
    ├── bootstrap/
    │   └── Terraform backend setup
    │
    ├── environments/
    │   └── Environment-specific configuration
    │
    ├── infrastructure/
    │   ├── AWS resource definitions
    │   ├── Lambda deployment configuration
    │   ├── EventBridge scheduling
    │   ├── IAM policies and roles
    │   └── S3 snapshot storage
    │
    └── modules/
        └── Reusable Terraform modules
```

### Repository Organization Decision

Note:

Lambda application code currently resides with Terraform infrastructure because the Lambda package is tightly coupled with deployment configuration.

Future iterations may separate application source and infrastructure code into independent directories as the project evolves.


## Design Decisions

### Snapshot-Based Drift Detection

CloudMortem uses a snapshot comparison model rather than directly evaluating changes against live AWS resources.

Each execution:
- Collects the current AWS inventory.
- Stores the inventory snapshot in Amazon S3.
- Compares the current snapshot against the previous snapshot.
- Reports created, deleted, and modified resources.

This approach keeps inventory collection, storage, and comparison logic separated, making the system easier to test and extend.

### Serverless Architecture

CloudMortem uses AWS Lambda with EventBridge scheduling because the workload is periodic and event-driven.

This avoids maintaining continuously running infrastructure while providing automatic execution when inventory scans are required.

### Infrastructure as Code

Terraform manages CloudMortem infrastructure to provide:
- Repeatable deployments.
- Version-controlled infrastructure changes.
- Automated validation through GitHub Actions.

### IAM Least Privilege

CloudMortem uses IAM roles and policies to control Lambda permissions required for AWS inventory collection.

Permissions are designed around the principle of granting only the access required for resource discovery while avoiding unnecessary privileges.

### Storage Design

Amazon S3 is used for inventory snapshot storage because snapshots are historical records that require durable, low-cost storage rather than frequent transactional updates.

## Status

MVP complete.

Current phase:

Production Hardening

Completed:

- Serverless AWS architecture
- Terraform infrastructure deployment
- GitHub Actions CI/CD pipeline
- Terraform plan/apply workflow
- Production approval workflow
- AWS OIDC authentication

Upcoming:

- Infrastructure security scanning
- Terraform quality gates
- Cost optimization improvements
- Operational runbooks
