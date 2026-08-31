# Interview Module 05 — Real Production Outage & Troubleshooting Scenarios

## Scenario 1: The Out-Of-Memory (OOM) Mystery in a Container
### Incident:
A Python backend service running in Kubernetes crashes intermittently under high traffic. `kubectl get pods` shows `CrashLoopBackOff` with exit code `137`.

### 🔍 Diagnostic Steps:
1. **Analyze Exit Code:** Exit code $137 = 128 + 9$ (`SIGKILL`). This proves the Linux kernel OOM Killer forcefully terminated the process because it exceeded its container memory limit (`resources.limits.memory`).
2. **Inspect Code:** Search for unbounded in-memory accumulations—such as calling `f.read()` or `f.readlines()` on large user uploads, or caching objects in global dictionaries without an LRU eviction policy.
3. **Remediation:** Replace batch reads with streaming generators, enforce streaming I/O, and tune Kubernetes memory limits and HPA (Horizontal Pod Autoscaler) metrics.

---

## Scenario 2: The Silent Pipeline Failure
### Incident:
A deployment script ran in GitHub Actions and printed `[ERROR] Database connection failed`, but the GitHub Actions step was marked as green/passed (`✅`), causing broken code to reach staging.

### 🔍 Diagnostic Steps:
1. **Root Cause:** The Python script caught the exception in a `try...except` block, printed the error message to stdout with `print()`, and exited naturally without setting a non-zero exit code (`sys.exit(1)`).
2. **Remediation:** In CI/CD scripts, whenever a critical error or threshold breach occurs, always invoke `sys.exit(1)` or let the exception bubble up so the container runtime registers a non-zero exit code.
