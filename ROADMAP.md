# 🗺️ Python for DevOps Progress Roadmap

Track your learning journey by checking off each topic as you complete the lesson, run the examples, and solve the exercises.

---

## 🟢 LEVEL 0 — Foundations
- [ ] **00-shell-vs-python-vs-ansible**
  - [ ] The DevOps Automation Triangle (Shell vs Python vs Ansible)
  - [ ] Choosing the right tool for the job (Decision Matrix)
  - [ ] Running Python scripts and understanding the interpreter
- [ ] **01-python-basics**
  - [ ] `01-variables-and-data-types`: Strings, Integers, Floats, Booleans
  - [ ] `02-strings-and-formatting`: f-strings, slicing, strip, split, replace
  - [ ] `03-numbers-and-math`: Memory thresholds, disk math, calculations
  - [ ] `04-conditionals-if-else`: Health checks, status code decisions, nested conditions
  - [ ] `05-lists-and-tuples`: Server lists, port ranges, iterating collections
  - [ ] `06-dictionaries-and-sets`: Server metadata, JSON objects, unique IP deduplication
  - [ ] `07-loops-for-while`: Polling services, retry loops, batch operations
  - [ ] `08-functions-and-scope`: Reusable check functions, parameters, return values
  - [ ] `09-modules-and-virtualenvs`: `pip`, `venv`, `requirements.txt`, structuring scripts

---

## 🟡 LEVEL 1 — Linux Systems & OS Automation
- [ ] **02-python-for-linux**
  - [ ] `01-sys-and-os-modules`: CLI arguments (`sys.argv`), path handling, system info
  - [ ] `02-subprocess-running-commands`: Executing `systemctl`, `df -h`, `docker`, capturing stdout/stderr
  - [ ] `03-process-management-psutil`: CPU, Memory, Disk, killing runaway processes
  - [ ] `04-environment-variables-secrets`: `os.environ`, reading API tokens securely
  - [ ] `05-signals-and-exit-codes`: `sys.exit()`, catching SIGTERM, graceful shutdowns

---

## 🟠 LEVEL 2 — Files, Logs, JSON & YAML
- [ ] **03-files-json-yaml**
  - [ ] `01-reading-writing-files`: Safe file I/O with `with open()`, file backups
  - [ ] `02-parsing-large-logs`: Streaming 10 GB logs line-by-line without memory crashes
  - [ ] `03-json-processing`: `json.loads()`, `json.dumps()`, parsing API responses
  - [ ] `04-yaml-and-config-parsing`: `PyYAML`, modifying Kubernetes manifests & Docker Compose
  - [ ] `05-csv-and-reports`: Generating CSV audit reports for compliance

---

## 🔵 LEVEL 3 — Networking & REST APIs
- [ ] **04-apis-and-networking**
  - [ ] `01-requests-and-rest-apis`: `GET`, `POST`, `PUT`, `DELETE`, HTTP status codes
  - [ ] `02-authentication-tokens-headers`: Bearer tokens, Basic Auth, Slack/GitHub API headers
  - [ ] `03-handling-retries-and-timeouts`: Resilient API polling, exponential backoff
  - [ ] `04-socket-and-port-checking`: TCP connection testing, port reachability checker

---

## 🟣 LEVEL 4 — Automation Tooling & CLI Development
- [ ] **05-automation**
  - [ ] `01-cli-tools-with-argparse`: Building professional CLI utilities (`--env`, `--dry-run`, `--verbose`)
  - [ ] `02-cron-and-scheduled-tasks`: Scheduling maintenance jobs and health checks
  - [ ] `03-logging-and-monitoring-alerts`: Python `logging` module vs `print()`, formatting syslog
  - [ ] `04-regex-for-devops-log-parsing`: Extracting IPs, HTTP status codes, UUIDs with `re`

---

## 🐳 LEVEL 5 — Docker Automation
- [ ] **06-docker**
  - [ ] `01-docker-sdk-basics`: Connecting to Docker daemon via `docker-py`
  - [ ] `02-inspecting-containers-and-images`: Filtering stopped containers, auditing images
  - [ ] `03-cleanup-and-monitoring-scripts`: Pruning dangling images, automated container restart

---

## ☸️ LEVEL 6 — Kubernetes Automation
- [ ] **07-kubernetes**
  - [ ] `01-k8s-client-pod-status`: In-cluster and kubeconfig auth, listing pods and nodes
  - [ ] `02-deployments-and-scaling`: Checking replica counts, updating image tags
  - [ ] `03-crashloopbackoff-detector`: Hunting failed pods and querying K8s events

---

## ☁️ LEVEL 7 — AWS & Cloud Automation
- [ ] **08-aws-cloud**
  - [ ] `01-boto3-ec2-management`: Listing instances, starting/stopping, filtering by tags
  - [ ] `02-s3-backup-automation`: Uploading build artifacts, configuring lifecycle rules
  - [ ] `03-cost-and-unused-resource-auditor`: Detecting unattached EBS volumes & stale snapshots

---

## 🚀 LEVEL 8 — CI/CD Pipeline Automation
- [ ] **09-ci-cd**
  - [ ] `01-pipeline-scripting-github-actions`: Python in GitHub Actions & GitLab CI
  - [ ] `02-artifact-versioning-and-tagging`: Semantic versioning calculator from git tags
  - [ ] `03-smoke-test-runner`: Automated post-deployment verification script

---

## 🛡️ LEVEL 9 — Testing, Debugging & Reliability
- [ ] **10-testing-debugging**
  - [ ] `01-debugging-common-errors`: Taxonomy of errors (`KeyError`, `FileNotFoundError`, `TypeError`)
  - [ ] `02-unit-testing-with-pytest`: Writing automated tests for DevOps automation
  - [ ] `03-mocking-apis-and-subprocesses`: Mocking external HTTP and Linux commands

---

## 🏗️ LEVEL 10 — Real-World Production Projects
- [ ] **11-real-world-projects**
  - [ ] `01-server-health-checker`: Full host metrics and services audit tool
  - [ ] `02-log-analyzer`: Production log aggregation & top errors reporter
  - [ ] `03-disk-monitor-alert`: Threshold monitoring with Slack webhook alerts
  - [ ] `04-api-health-monitor`: Multi-endpoint latency and status SLA checker
  - [ ] `05-k8s-cluster-auditor`: Kubernetes cluster security & resource compliance tool
  - [ ] `06-devops-automation-toolkit-capstone`: Production multi-command CLI utility

---

## 💼 LEVEL 11 & 12 — Interview Preparation & Capstone
- [ ] **12-interview-preparation**
  - [ ] `01-python-fundamentals-questions.md` (50 Core Questions & Answers)
  - [ ] `02-linux-and-subprocess-questions.md` (30 OS & Process Automation Questions)
  - [ ] `03-apis-and-cloud-questions.md` (30 API, AWS & K8s Questions)
  - [ ] `04-shell-vs-python-vs-ansible-questions.md` (20 Tool Decision Scenarios)
  - [ ] `05-troubleshooting-scenarios.md` (30 Real Production Outage Scenarios)
  - [ ] `06-mock-interview-guide.md` (Interactive Practice Framework with Scoring Rubric)
