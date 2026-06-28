# CloudMortem

Serverless AWS infrastructure inventory and drift detection platform.

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

AWS EventBridge
        |
        v
AWS Lambda
        |
        v
Resource Discovery
        |
        v
Inventory Snapshot
        |
        v
S3 Storage
        |
        v
Drift Detection

## Tech Stack

- AWS Lambda
- Amazon S3
- Terraform
- Python
- IAM
- EventBridge

## Status

MVP complete.
