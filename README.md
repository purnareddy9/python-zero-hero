# 🐍 Python for DevOps: Zero to Production

> A hands-on, practical course designed specifically for **DevOps Engineers, SREs, System Administrators, and Cloud Engineers**.

---

## 🎯 What is this Course?

This is not a general software engineering course. You will not build consumer web applications, mobile apps, or games. 

Instead, this course teaches the exact Python skills that a **Senior DevOps Engineer (5–8 years experience)** uses daily to:
- Automate Linux systems and servers.
- Interact with cloud infrastructure (AWS) and container platforms (Docker & Kubernetes).
- Parse massive log files, JSON, YAML, and CSV reports.
- Build reliable CI/CD pipeline automation scripts.
- Integrate with REST APIs (Slack, GitHub, PagerDuty, Jira).
- Confidently answer technical Python questions in DevOps interviews.

---

## 🧭 Course Roadmap

Follow the numbered modules in sequence. Check off your progress in [ROADMAP.md](ROADMAP.md).

```text
LEVEL 0  ──► 00-shell-vs-python-vs-ansible  (The Automation Landscape)
         ──► 01-python-basics               (Zero to Core Scripting)
LEVEL 1  ──► 02-python-for-linux            (OS, Subprocess, Psutil, Signals)
LEVEL 2  ──► 03-files-json-yaml             (Log Streaming, JSON, YAML, CSV)
LEVEL 3  ──► 04-apis-and-networking         (REST APIs, Requests, Auth, Sockets)
LEVEL 4  ──► 05-automation                  (CLI Tools, Logging, Cron, Regex)
LEVEL 5  ──► 06-docker                      (Docker SDK, Container Management)
LEVEL 6  ──► 07-kubernetes                  (K8s Client, Pod & Cluster Health)
LEVEL 7  ──► 08-aws-cloud                   (Boto3, EC2, S3, Cost Audit)
LEVEL 8  ──► 09-ci-cd                       (GitHub Actions, Artifacts, Smoke Tests)
LEVEL 9  ──► 10-testing-debugging           (Pytest, Mocking, Production Debugging)
LEVEL 10 ──► 11-real-world-projects         (6 Production DevOps Projects)
LEVEL 11 ──► 12-interview-preparation       (200+ Categorized Interview Questions)
LEVEL 12 ──► Capstone Project               (The DevOps Automation Toolkit CLI)
```

---

## 📂 Lesson Structure

Every lesson directory contains:
- `lesson.md`: Detailed visual guide with Mermaid diagrams, zero-level explanations, Shell vs Python vs Ansible comparisons, and interview prep.
- `example.py`: Runnable, production-ready Python example.
- `exercise.py`: Hands-on exercise template with hints.
- `solution.py`: Complete verified solution with comments.

---

## ⚡ Quickstart: Setting Up Your Environment

### 1. Clone & Open
Open this folder in **Visual Studio Code**.

### 2. Create a Virtual Environment
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run an Example
```bash
python 00-shell-vs-python-vs-ansible/example.py
```

---

## 📖 Viewing as a Local Documentation Portal (Optional)

You can view this entire course as a fast, searchable documentation site using MkDocs:

```bash
pip install mkdocs-material
mkdocs serve
```

Then open `http://127.0.0.1:8000` in your browser.
