# Interview Module 04 — Tool Decision Scenarios: Shell vs Python vs Ansible

## Scenario 1: Parsing a 50 GB log file and extracting unique malicious IPs
### 🗣️ Senior DevOps Decision:
> **Choice: Python**
> **Rationale:** *"Shell `awk | sort | uniq` will create massive temporary files in `/tmp` and exhaust disk I/O. Ansible is completely unsuitable for file streaming. Python using a streaming line iterator (`with open() as f: for line in f:`) and a Python `set` in memory parses 50 GB in a single linear O(N) pass using less than 30 MB of RAM."*

---

## Scenario 2: Configuring SSH hardening, UFW firewall, and NTP across 300 Linux virtual machines
### 🗣️ Senior DevOps Decision:
> **Choice: Ansible**
> **Rationale:** *"Writing Python scripts with Paramiko to SSH into 300 servers requires manually building SSH connection pools, handling partial failures, and writing idempotency checks. Ansible is specifically built for declarative multi-node configuration management and ensures idempotency out of the box."*

---

## Scenario 3: Quick CI/CD step to build a Docker container and push to ECR
### 🗣️ Senior DevOps Decision:
> **Choice: Shell (Bash)**
> **Rationale:** *"A 3-line shell script (`docker build -t $TAG . && docker push $TAG`) is direct, zero-overhead, and natively supported on all CI runners without needing Python virtualenvs or SDK boilerplate."*

---

## Scenario 4: Building an interactive internal CLI tool for developers to spin up ephemeral staging environments
### 🗣️ Senior DevOps Decision:
> **Choice: Python**
> **Rationale:** *"Python's `argparse` provides automated `--help` generation, subcommands, type checking, and rich terminal output. Python connects directly to Kubernetes and AWS SDKs with full unit test coverage via `pytest`."*
