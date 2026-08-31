# Interview Module 06 — Senior DevOps Python Mock Interview Framework

## 🎯 Purpose
Use this interactive guide to evaluate your readiness for Senior DevOps / SRE technical interviews.

---

## ⏱️ Structure of a Senior DevOps Python Interview (45–60 mins)

```text
1. Introduction & Operational Background         (5 mins)
2. Tooling Architecture & Decision Scenarios     (10 mins)  [Shell vs Python vs Ansible]
3. Live Scripting / Code Triage Exercise         (25 mins)  [Log parsing, Subprocess, API retries]
4. Distributed Systems & Reliability Follow-up   (10 mins)  [Timeouts, OOMs, Secret management]
5. Candidate Questions                           (5 mins)
```

---

## 📋 Evaluation Rubric

| Competency | Strong Candidate (Senior Level) | Red Flag (Junior / Inexperienced) |
| :--- | :--- | :--- |
| **Error Handling** | Catches specific exceptions, uses timeouts, handles 429/5xx retries | Uses bare `except:`, forgets timeouts, assumes APIs never fail |
| **Memory Awareness** | Streams large logs with line iterators, avoids O(N^2) allocations | Uses `f.read()` or `f.readlines()` on unknown file sizes |
| **Security & Secrets** | Reads from `os.environ`, masks secrets in logs, uses `shell=False` | Hardcodes API tokens in `.py` files, uses `shell=True` with strings |
| **Tool Selection** | Knows when to use Bash vs Python vs Ansible accurately | Tries to write custom SSH scripts in Python instead of Ansible |
| **Testing** | Writes unit tests with `pytest` and mocks external APIs | Tests manually by calling production endpoints directly |

---

## 🎤 Practice Questions to Answer Out Loud:
1. *"Walk me through how you would automate the rotation of expired IAM access keys across 50 AWS accounts using Python."*
2. *"A Python automation script works on your laptop but fails with `PermissionDenied` inside a Kubernetes Pod. How do you troubleshoot it?"*
3. *"Why would you choose `urllib3.util.Retry` with exponential backoff over a basic `while True` retry loop?"*
