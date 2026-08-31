# Lesson 03 — JSON Processing in DevOps

## 🎯 What will I learn?
You will master reading, parsing, manipulating, and writing **JSON (JavaScript Object Notation)** files and API payloads in Python using the built-in `json` module (`json.loads()`, `json.dumps()`, `json.load()`, `json.dump()`).

---

## 🤔 Why does a DevOps engineer need this?
JSON is the lingua franca of DevOps:
- Every cloud provider API (AWS, GCP, Azure) returns JSON.
- `docker inspect <container>` and `kubectl get pods -o json` output JSON.
- Monitoring alert payloads (PagerDuty, Slack Webhooks, Prometheus Alertmanager) are JSON.
- CI/CD build reports and vulnerability scanner results (Trivy, Snyk) are formatted in JSON.

---

## 🧠 Mental model

```mermaid
flowchart LR
    API["API JSON String: '{\"status\": 200}'"] -->|json.loads| Dict["Python Dict: {'status': 200}"]
    Dict -->|json.dumps| Payload["Outgoing Webhook JSON String"]
```

---

## 📖 Concept

### The 4 Core JSON Functions

| Function | What it does | Input / Output |
| :--- | :--- | :--- |
| `json.loads(s)` | Parse JSON from a **string** | `str` -> `dict`/`list` |
| `json.dumps(obj, indent=2)` | Convert Python object to a formatted JSON **string** | `dict`/`list` -> `str` |
| `json.load(f)` | Read and parse JSON directly from a **file stream** | File stream -> `dict`/`list` |
| `json.dump(obj, f, indent=2)` | Write a Python object directly to a JSON **file** | `dict`/`list` -> File stream |

---

## 💻 Simple example

```python
import json

# String to Python Dict
raw_json = '{"cluster": "prod-east", "nodes": 10}'
data = json.loads(raw_json)
print(data["cluster"])  # 'prod-east'

# Python Dict to Pretty-Printed JSON String
data["nodes"] += 2
pretty_str = json.dumps(data, indent=2)
print(pretty_str)
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Docker Inspect Parser & Vulnerability Scanner JSON Aggregator
"""
import json

# Simulating raw JSON output from a container vulnerability scan
mock_scan_report = """
{
  "image": "myregistry.io/payment-api:v2.1.0",
  "scan_time": "2026-08-31T10:15:00Z",
  "vulnerabilities": [
    {"cve": "CVE-2026-1001", "severity": "HIGH", "package": "openssl"},
    {"cve": "CVE-2026-1002", "severity": "LOW", "package": "curl"},
    {"cve": "CVE-2026-1003", "severity": "CRITICAL", "package": "glibc"}
  ]
}
"""

def parse_security_scan(raw_json_str):
    print("========================================")
    print("     CONTAINER SECURITY AUDIT REPORT    ")
    print("========================================")
    
    # 1. Parse string into Python dictionary
    data = json.loads(raw_json_str)
    
    image = data.get("image")
    vulns = data.get("vulnerabilities", [])
    
    print(f"Target Image: {image}")
    print(f"Total CVEs  : {len(vulns)}\n")
    
    critical_cves = [v for v in vulns if v.get("severity") == "CRITICAL"]
    high_cves = [v for v in vulns if v.get("severity") == "HIGH"]
    
    print(f"Critical Severity: {len(critical_cves)}")
    print(f"High Severity    : {len(high_cves)}")
    print("----------------------------------------")
    
    if critical_cves:
        print("[!] BLOCKING DEPLOYMENT: Critical CVEs detected:")
        for cve in critical_cves:
            print(f"    - {cve['cve']} in package '{cve['package']}'")
        return False
        
    print("[+] Security gate passed. No critical vulnerabilities.")
    return True

if __name__ == "__main__":
    passed = parse_security_scan(mock_scan_report)
    print("========================================")
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
     CONTAINER SECURITY AUDIT REPORT    
========================================
Target Image: myregistry.io/payment-api:v2.1.0
Total CVEs  : 3

Critical Severity: 1
High Severity    : 1
----------------------------------------
[!] BLOCKING DEPLOYMENT: Critical CVEs detected:
    - CVE-2026-1003 in package 'glibc'
========================================
```

---

## 🔍 Line-by-line explanation
- `data = json.loads(raw_json_str)`: Deserializes the JSON string into native Python dictionaries and lists.
- `[v for v in vulns if v.get("severity") == "CRITICAL"]`: Slices out high-severity objects using list comprehension.
- `json.dumps(..., indent=2)`: Produces clean, readable output for Slack webhooks or audit logs.

---

## 🐚 Shell equivalent

```bash
# In Shell, parsing JSON requires jq:
echo '$mock_scan_report' | jq '.vulnerabilities[] | select(.severity=="CRITICAL")'
```
*Why Python is better for pipelines:* While `jq` is great for quick terminal filters, writing multi-step conditional deployment decisions with loops and retries in `jq` becomes unreadable. Python provides full programmatic control.

---

## ⚙️ Ansible equivalent

```yaml
- name: Parse scan facts
  ansible.builtin.set_fact:
    criticals: "{{ scan_result.vulnerabilities | selectattr('severity', 'equalto', 'CRITICAL') | list }}"
```

---

## 🏆 Which one should I use?
- Use **`jq`** for 1-liner terminal queries (`kubectl ... | jq .status`).
- Use **Python `json`** for pipeline gates, custom alert webhooks, and transformation between different API payloads.

---

## ⚠️ Common mistakes
1. **Confusing `json.load()` with `json.loads()`:**
   - `json.load(f)` expects a **file object**.
   - `json.loads(s)` expects a **string** (the `s` stands for string).
2. **Invalid JSON syntax causing `json.JSONDecodeError`:**
   - Single quotes (`{'key': 'val'}`) are invalid in JSON. JSON requires double quotes (`{"key": "val"}`).

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Given a JSON string of microservices and their replica states, parse the JSON, identify any service where `available_replicas < desired_replicas`, and write a failure report to `incident.json` using `json.dump()`.

---

## 💡 Hint
Loop over services, check `meta["available"] < meta["desired"]`, and save results using `with open("incident.json", "w") as f: json.dump(report, f, indent=2)`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "What is the difference between `json.load()` and `json.loads()` in Python, and how do you handle malformed JSON from an external API?"
> **Interviewer Focus:** Testing basic Python standard library knowledge and exception handling around `json.JSONDecodeError`.

---

## 🗣️ How to answer in an interview
> *"`json.loads()` (load string) deserializes a JSON-formatted string from memory into Python objects, whereas `json.load()` reads and deserializes directly from an open file stream object. When communicating with external APIs, network glitches or error proxies can return HTML error pages instead of JSON. I always wrap JSON parsing in a `try...except json.JSONDecodeError` block to log the raw payload and handle the API failure gracefully without crashing the pipeline."*

---

## 📝 What I should remember
- `loads` = load from String.
- `dumps` = dump to String (use `indent=2` for pretty printing).
- `load` / `dump` = directly read/write from File streams.
- Always catch `json.JSONDecodeError` when parsing external payloads.
