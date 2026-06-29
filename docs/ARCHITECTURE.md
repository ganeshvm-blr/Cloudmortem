# CloudMortem Architecture

## Overview

CloudMortem is a serverless AWS infrastructure inventory and drift detection platform.

The system periodically collects AWS resource information, stores inventory snapshots, and compares changes against previous states to identify infrastructure drift.

---

# Runtime Architecture

```text
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

##CI/CD Deployment Architecture

CloudMortem uses GitHub Actions to implement a controlled infrastructure deployment workflow.

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions Pipeline
    |
    +-------------------------+
    |                         |
    v                         v
Python Validation       Terraform Validation
                                |
                                v
                        Terraform Plan
                                |
                                v
                    Artifact Storage
                                |
              +-----------------+
              |
              v
      Terraform Binary Plan

              |
              v

      Lambda Deployment Package

              |
              v

      Production Approval Gate

              |
              v

          Terraform Apply

              |
              v

        AWS Infrastructure

##Infrastructure Components
AWS Lambda

Purpose:

Execute inventory collection.
Process AWS resource data.
Generate drift comparison results.

Runtime:

Python 3.12

Amazon EventBridge

Purpose:

Schedule automated inventory collection.
Trigger Lambda execution.

Amazon S3

Purpose:

Store historical inventory snapshots.
Provide durable storage for drift comparison data.

Amazon CloudWatch

Purpose:

Store Lambda execution logs.
Provide operational visibility.

Infrastructure as Code

Terraform manages:

Lambda functions.
IAM roles and policies.
EventBridge scheduling.
CloudWatch resources.
S3 storage.

Infrastructure changes are version controlled through Git.

##Deployment Security Model

CloudMortem uses GitHub Actions OpenID Connect authentication.

Authentication flow:

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

Benefits:

No AWS access keys stored in GitHub.
Short-lived credentials.
Reduced credential exposure risk.


##Deployment Controls

Production deployments follow:

Code Change

      |

Validation

      |

Terraform Plan

      |

Artifact Storage

      |

Production Approval

      |

Terraform Apply


The Terraform binary plan and Lambda deployment package are stored as immutable artifacts to ensure the deployed infrastructure matches the reviewed changes.


##Design Principles

Infrastructure as Code

Terraform is the single source of truth for AWS infrastructure.

Least Privilege

IAM permissions are designed around required functionality only.

Controlled Deployment

Production infrastructure changes require validation and approval before execution.

Serverless First

CloudMortem uses managed AWS services to reduce operational overhead.
