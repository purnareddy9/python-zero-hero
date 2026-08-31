# Lesson 01 — REST APIs and the `requests` Module

## 🎯 What will I learn?
You will learn how to interact with modern HTTP/REST APIs using Python's famous `requests` library. You will master HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`), inspect status codes (`200`, `201`, `404`, `500`), send query parameters, and parse JSON responses.

---

## 🤔 Why does a DevOps engineer need this?
Modern infrastructure is entirely API-driven:

- Querying GitHub / GitLab APIs for commit status and release tags.
- Triggering Jenkins build jobs via REST endpoints.
- Sending incident alerts to Slack, Microsoft Teams, or PagerDuty webhooks.
- Probing microservice `/healthz` endpoints in canary deployment verifications.

---

## 🧠 Mental model

```mermaid
flowchart LR
    Python["requests.get('https://api.github.com/repos/org/app')"] --> Internet((Internet / VPC))
    Internet --> Server[GitHub REST API]
    Server -->|HTTP 200 OK + JSON Payload| Response[response.status_code == 200<br/>response.json()]
```

---

## 📖 Concept

### The HTTP Verbs in DevOps

| Verb | `requests` Method | DevOps Purpose |
| :--- | :--- | :--- |
| `GET` | `requests.get(url)` | Query status, fetch alerts, list cloud resources |
| `POST` | `requests.post(url, json=data)` | Trigger CI build, post Slack alert, create ticket |
| `PUT` / `PATCH` | `requests.put(url, json=data)` | Update deployment configuration, toggle feature flag |
| `DELETE` | `requests.delete(url)` | Remove stale image from registry, terminate runner |

---

## 💻 Simple example

```python
import requests

response = requests.get("https://httpbin.org/get", params={"env": "prod"}, timeout=5)
print(f"Status Code: {response.status_code}")
data = response.json()
print(f"Origin IP  : {data['origin']}")
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Microservice Health Probe & Slack Alert Webhook Dispatcher
"""
import requests
import json
import time

def probe_health_endpoint(url, timeout_sec=3):
    """
    Probes an HTTP health endpoint and returns (is_healthy, latency_ms, status_code).
    """
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout_sec)
        latency_ms = round((time.time() - start_time) * 1000, 2)
        is_healthy = response.status_code == 200
        return is_healthy, latency_ms, response.status_code
    except requests.exceptions.Timeout:
        return False, timeout_sec * 1000, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return False, 0.0, "CONNECTION_REFUSED"

def send_mock_slack_alert(webhook_url, service_name, status_code, latency_ms):
    """
    Constructs a JSON webhook payload and posts to a notification channel.
    """
    payload = {
        "text": f"🚨 *SERVICE OUTAGE ALERT*: `{service_name}` is DOWN!",
        "attachments": [
            {
                "color": "danger",
                "fields": [
                    {"title": "Service", "value": service_name, "short": True},
                    {"title": "Status Code", "value": str(status_code), "short": True},
                    {"title": "Probe Latency", "value": f"{latency_ms} ms", "short": True},
                    {"title": "Action", "value": "Traffic automatically routed away", "short": True}
                ]
            }
        ]
    }
    
    print(f"[*] Posting Webhook to Slack URL: {webhook_url}")
    print(f"    Payload: {json.dumps(payload, indent=2)}")
    
    # In production: requests.post(webhook_url, json=payload, timeout=5)
    return True

if __name__ == "__main__":
    print("========================================")
    print("      API PROBE & ALERT SYSTEM          ")
    print("========================================")
    
    test_endpoints = [
        ("Public JSON API", "https://httpbin.org/status/200"),
        ("Simulated 500 Error", "https://httpbin.org/status/500")
    ]
    
    for name, url in test_endpoints:
        print(f"[*] Probing {name} ({url})...")
        healthy, latency, code = probe_health_endpoint(url)
        
        if healthy:
            print(f"    [+] HEALTHY: HTTP {code} (Latency: {latency} ms)\n")
        else:
            print(f"    [!] UNHEALTHY: HTTP {code} (Latency: {latency} ms)")
            send_mock_slack_alert(
                webhook_url="https://hooks.slack.com/services/T00/B00/XXXX",
                service_name=name,
                status_code=code,
                latency_ms=latency
            )
            print()
            
    print("========================================")
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
      API PROBE & ALERT SYSTEM          
========================================
[*] Probing Public JSON API (https://httpbin.org/status/200)...
    [+] HEALTHY: HTTP 200 (Latency: 142.12 ms)

[*] Probing Simulated 500 Error (https://httpbin.org/status/500)...
    [!] UNHEALTHY: HTTP 500 (Latency: 138.45 ms)
[*] Posting Webhook to Slack URL: https://hooks.slack.com/services/T00/B00/XXXX
    Payload: {
      "text": "🚨 *SERVICE OUTAGE ALERT*: `Simulated 500 Error` is DOWN!",
      ...
    }

========================================
```

---

## 🔍 Line-by-line explanation
- `response = requests.get(url, timeout=timeout_sec)`: **Always pass a `timeout`!** Never make an HTTP request in production without a timeout limit.
- `response.json()`: Automatically parses response body from JSON into a Python dictionary.
- `requests.exceptions.ConnectionError`: Catches DNS failures, refused connections, or downed gateways cleanly.

---

## 🐚 Shell equivalent

```bash
# In Bash, making API calls requires curl:
STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://httpbin.org/status/200)
if [ "$STATUS" -ne 200 ]; then
    curl -X POST -H "Content-Type: application/json" -d '{"text":"Outage"}' "$SLACK_WEBHOOK"
fi
```
*Why Python is better:* In Shell, constructing nested JSON payloads for Slack/Jira with special character escaping easily breaks. In Python, passing `json=payload` automatically sets headers and escapes strings safely.

---

## ⚙️ Ansible equivalent

```yaml
- name: Probe API endpoint
  ansible.builtin.uri:
    url: https://httpbin.org/status/200
    method: GET
    status_code: 200
```

---

## 🏆 Which one should I use?
- Use **Python `requests`** whenever interacting with REST APIs that require token authentication, JSON schema transformations, retries, and conditional logic.

---

## ⚠️ Common mistakes
1. **Omitting the `timeout` parameter:**

   - Default `requests.get()` has NO timeout! If a remote server hangs, your Python script will hang forever, blocking your CI/CD runner.
2. **Not checking `response.status_code` before calling `response.json()`:**

   - If an API returns a 502 Bad Gateway HTML page, `response.json()` will throw `json.JSONDecodeError`.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Write a function `check_api_endpoint(url)` that requests `https://httpbin.org/json`. Verify that `status_code == 200`, extract the `"slideshow"` -> `"title"` key from the JSON, and return it. Handle `requests.exceptions.RequestException`.

---

## 💡 Hint
Use `try...except requests.exceptions.RequestException as e:`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "What happens if you don't specify a `timeout` in Python's `requests` library in a production pipeline?"
> **Interviewer Focus:** Testing production resilience and prevention of thread/runner starvation.

---

## 🗣️ How to answer in an interview
> *"By default, Python's `requests` calls do not have a timeout limit. If a target server drops packets, hangs, or experiences network partition, the connection socket stays open indefinitely. In a CI/CD runner, Kubernetes cronjob, or worker process, this blocks execution indefinitely, causing pipeline deadlocks and resource starvation. In production, we always explicitly specify `timeout=(connect_timeout, read_timeout)`, such as `timeout=(3.05, 10)`."*

---

## 📝 What I should remember
- Always set a `timeout` (e.g. `timeout=5`).
- Use `response.json()` to parse response bodies.
- Use `json=payload` in `requests.post()` to automatically serialize data and set `Content-Type: application/json`.
- Catch `requests.exceptions.RequestException` to handle all network failures.
