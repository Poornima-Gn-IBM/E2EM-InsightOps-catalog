# E2EM-InsightOps-catalog
# E2EM InsightOps

## Purpose
E2EM InsightOps ensures that observability is not only deployed but actively working, measurable, and compliant within Sovereign Core environments.

## Key Capabilities
- Discovers applications in a namespace
- Validates E2EM trace flow
- Identifies non-monitored or misconfigured services
- Provides adoption metrics via API

## Sovereign Design
- Runs fully in-cluster
- No outbound internet dependency
- No secrets stored in Git
- GitOps-based deployment via ArgoCD

## Parameters

| Parameter            | Required | Description |
|---------------------|----------|-------------|
| namespace           | Yes      | Target namespace |
| e2em_backend_url    | Yes      | Trace backend endpoint |
| scan_interval       | No       | Scan frequency (seconds) |

## API Endpoints

- `/adoption-summary`
- `/applications`

## Architecture

```mermaid
flowchart LR
  A[CSB] --> B[GitOps Repo]
  B --> C[ArgoCD]
  C --> D[Kubernetes Cluster]
  D --> E[InsightOps]
  D --> F[Applications]
  F --> G[E2EM Backend]
  E --> F
  E --> G
