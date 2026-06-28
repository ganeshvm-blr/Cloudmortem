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

## Tech Stack

- AWS Lambda
- Amazon S3
- Terraform
- Python
- IAM
- EventBridge

## CI/CD Workflow

CloudMortem uses GitHub Actions to automatically validate application and infrastructure changes.

Current pipeline:

Developer
|
|
Git Push
|
|
GitHub Actions
|
+-- Python syntax validation
|
+-- Python tests
|
+-- Terraform formatting check
|
+-- Terraform validation


The validation pipeline helps prevent invalid application changes and Terraform configuration issues from reaching deployment stages.

Future improvements include adding Terraform plan generation and controlled deployment workflows with manual approval gates.


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
