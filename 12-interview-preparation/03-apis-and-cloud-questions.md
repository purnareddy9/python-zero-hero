# Interview Module 03 — REST APIs, Kubernetes & Cloud Automation Questions

## Q1: How do you implement robust retries with exponential backoff and jitter for AWS or Kubernetes APIs?
### 🗣️ Natural Senior DevOps Answer:
> *"When calling cloud APIs, transient 5xx errors or 429 rate limits are common. We implement a retry policy that doubles the delay on each failed attempt (`delay = base * (2 ** attempt)`). We add random 'jitter' to avoid the thundering herd problem where hundreds of worker instances retry at the exact same millisecond. In Python, we configure `urllib3.util.Retry` directly on our `requests.Session` adapter, targeting transient status codes like 429, 500, 502, 503, and 504 while failing fast on permanent 400/401/404 errors."*

---

## Q2: How do you authenticate Boto3 in production without storing static access keys?
### 🗣️ Natural Senior DevOps Answer:
> *"Storing static AWS access keys in code or configuration files is a major security vulnerability. In modern cloud architectures, we rely on IAM Roles: in AWS EC2 we attach IAM Instance Profiles, and in Kubernetes (EKS) we use IAM Roles for Service Accounts (IRSA). Boto3 automatically retrieves temporary, short-lived STS credentials from the metadata service or projected token volume. This eliminates credential leaks and handles key rotation automatically."*

---

## Q3: How do you detect and troubleshoot CrashLoopBackOff pods programmatically using the Kubernetes Python client?
### 🗣️ Natural Senior DevOps Answer:
> *"We do not rely solely on `pod.status.phase` because a crashlooping pod often remains in the 'Running' phase from a cluster scheduling standpoint. Instead, we iterate over `pod.status.container_statuses` and inspect `cs.state.waiting.reason`. If it equals `'CrashLoopBackOff'`, we query `cs.last_state.terminated.exit_code` (e.g. exit code 137 indicates OOMKilled, exit code 1 indicates application exception). We can then call `CoreV1Api.read_namespaced_pod_log(previous=True)` to extract the crash logs from the dead container."*
