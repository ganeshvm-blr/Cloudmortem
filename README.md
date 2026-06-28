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

## Status

MVP complete.
