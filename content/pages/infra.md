Title: Infrastructure
Date: 2026-07-13
Modified: 2026-07-13
Category: 
Tags: infrastructure, docker, aws, observability, splunk, ci-cd
Status: published
Slug: infra

Notes on running systems in production — containerization, deployment pipelines, monitoring, and the operational patterns that keep things stable.

---

## Containerization & Docker

Practical patterns for running containers without fighting the tooling.

- [Docker: Automatically Exiting Containers](../docker/docker-automatically-exiting.md) — why your container exits immediately and how to fix it
- [Docker: Exec and Writing Results to a Variable](../docker/docker-exec-write-result-to-a-variable.md) — capturing command output from inside a container
- [Docker Windows Tips & Tricks](../docker/Docker%20Windows%20Tips-Trics.md) — Windows-specific gotchas and workflows
- [Docker Network Issues](../docker-network-issues.md) — connectivity problems and how to diagnose them
- [Install Chrome on Amazon Linux 2 Workspace](../Install-Chrome-on-Amazon-Linux2-Workspace.md) — headless browser setup for automation
- [Install Docker on Amazon Linux Workspace](../Install-Docker-On-Amazon-linux-workspace.md) — quickstart for AL2 environments

## Deployment & CI/CD

Pipeline patterns that keep deployments predictable and reversible.

- [Host a Static Site Using Pelican, Amazon S3](../Host%20a%20Static%20Site%20using%20Pelican%20,%20Amzon%20S3.md) — content-as-code publishing without a CMS
- [Pelican Static Site: Continuous Delivery to AWS S3](../PelicanStaticSite-continous-delivery-to-aws-s3.md) — GitHub Actions workflow for automated deployment
- [GitLab: Generate Release Notes — CI/CD](../Gitlab%20Generate%20Release%20Notes-CICD.md) — automated changelog generation
- [Install Consul with Minikube, Helm, Docker](../install-consul-with-minikube-helm-docker.md) — service discovery in Kubernetes

## Observability & Monitoring

You can't fix what you can't see. These notes cover structured logging, metrics, and alerting patterns.

- [Splunk: Quick Reference](../Splunk-Quick-Reference.md) — core SPL queries and search patterns
- [Splunk: Core Certified User — Certification Tips](../Splunk-Core-Certified-User-Certification-Tips.md) — what to focus on when studying
- [New Relic: Quick Reference](../New%20Relic%20Quick%20Reference.md) — APM basics and query syntax

## Workspace & Dev Environment

Setting up reproducible development environments without losing time to config drift.

- [Windows: WSL Reset Root Password](../windows-wsl-reset-root-password.md) — recovery when you lock yourself out
- [Generate Bulk XML Files for Load Testing](../Generate%20Bulk%20XML%20files%20for%20Load%20testing.md) — Raven tool for middleware stress testing

---

## Patterns Worth Remembering

**Containers should fail fast.** If a container exits immediately, it's usually a missing entrypoint command or a misconfigured health check. Fix the root cause, don't paper over it with `sleep 3600`.

**Infrastructure as code isn't optional.** If you're manually configuring servers, you're creating snowflakes. Codify everything, even if it feels like overkill today.

**Observability is a feature, not an afterthought.** Structured logging, metrics, and tracing aren't "nice to have" — they're what let you debug production at 2 AM without losing your mind.
