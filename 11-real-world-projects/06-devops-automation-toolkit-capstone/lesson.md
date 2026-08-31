# Project 06 — Capstone: The DevOps Automation Toolkit CLI

## 🎯 What will I learn?
You will build a complete, modular, enterprise-grade **DevOps Automation CLI Toolkit** that brings together everything you have learned throughout this course: Linux system health, disk management, streaming log analysis, Docker container operations, Kubernetes cluster auditing, and AWS cloud FinOps.

---

## 🧠 Architecture Overview

```text
devops-tool/
├── main.py        # Central CLI Entrypoint with Argparse Subcommands
├── health.py      # Host CPU, Memory, Uptime diagnostics
├── disk.py        # Multi-mount disk auditor & retention purger
├── logs.py        # Streaming log parser & error aggregator
├── docker_ops.py  # Container lifecycle & dangling image pruner
├── k8s_ops.py     # Kubernetes pod status & crash detector
└── aws_ops.py     # AWS EC2 cost optimizer & unattached EBS auditor
```

---

## 💻 CLI Commands

```bash
# System Health Subcommand
python main.py health

# Disk Audit Subcommand
python main.py disk --threshold 85 --purge-dry-run

# Log Analyzer Subcommand
python main.py logs --file /var/log/app.log --top 5

# Docker Operations
python main.py docker --prune

# Kubernetes Operations
python main.py k8s --namespace production

# AWS Operations
python main.py aws --region us-east-1
```

---

## 📂 Implementation Modules

Explore the modular implementations in this directory:
- `main.py`: Dispatches subcommands cleanly to dedicated modules.
- Run `python main.py --help` to see the full operational menu.
