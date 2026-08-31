# Lesson 03 — Mocking External APIs, Subprocesses, and Cloud SDKs

## 🎯 What will I learn?
You will learn how to write unit tests for scripts that call external services without actually making network calls or running real system commands, using `unittest.mock` (`patch`, `MagicMock`, `mock_subprocess`).

---

## 🤔 Why does a DevOps engineer need this?
Testing infrastructure code poses a unique challenge:
- You cannot actually call `boto3.client('ec2').terminate_instances()` during a unit test run in CI!
- You cannot depend on live third-party APIs (Slack, GitHub) being available while tests run in an isolated offline runner.
- **Mocking** intercepts the external call, replaces it with a simulated fake response, and verifies that your Python logic processes the response correctly.

---

## 🧠 Mental model

```mermaid
flowchart LR
    Test["Pytest Test Runner"] --> Mock["unittest.mock.patch('requests.get')"]
    Mock --> Intercept["Intercepts HTTP Call -> Returns Fake 500 JSON"]
    Intercept --> PythonScript["Script processes simulated outage"]
    PythonScript --> Assert["Assert: Alert sent and exit code 1 returned"]
```

---

## 📖 Concept

Use `unittest.mock.patch` to mock functions or objects during tests.

```python
from unittest.mock import patch, MagicMock

# Mocking requests.get
@patch("requests.get")
def test_api_call(mock_get):
    # Setup fake return object
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"status": "HEALTHY"}
    mock_get.return_value = fake_response
    
    # Call your actual function
    result = check_health("https://api.internal/health")
    assert result is True
```

---

## 💻 Simple example

```python
from unittest.mock import MagicMock

fake_ec2 = MagicMock()
fake_ec2.describe_instances.return_value = {"Reservations": []}

resp = fake_ec2.describe_instances()
print("Mocked AWS response:", resp)
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Unit Testing with Mocked Subprocesses and HTTP APIs
Demonstrates testing Linux command execution and REST APIs without external dependencies.
"""
import subprocess
import requests
from unittest.mock import patch, MagicMock

# 1. Functions under test
def check_disk_is_critical(mount_point="/"):
    """Runs df -h via subprocess and checks if usage > 85%."""
    proc = subprocess.run(["df", "-h", mount_point], capture_output=True, text=True)
    lines = proc.stdout.strip().split("\n")
    if len(lines) < 2:
        return False
    # Mock line format: /dev/sda1 100G 88G 12G 88% /
    usage_str = lines[1].split()[4].replace("%", "")
    return int(usage_str) >= 85

def query_slack_webhook_alert(webhook_url, message):
    """Sends POST request to Slack webhook."""
    payload = {"text": message}
    res = requests.post(webhook_url, json=payload, timeout=3)
    return res.status_code == 200

# 2. Pytest Unit Tests using unittest.mock.patch
@patch("subprocess.run")
def test_check_disk_critical_true(mock_subproc):
    # Provide fake stdout string simulating an 88% full disk
    fake_proc = MagicMock()
    fake_proc.returncode = 0
    fake_proc.stdout = "Filesystem Size Used Avail Use% Mounted on\n/dev/sda1 100G 88G 12G 88% /\n"
    mock_subproc.return_value = fake_proc
    
    assert check_disk_is_critical("/") is True

@patch("subprocess.run")
def test_check_disk_healthy(mock_subproc):
    fake_proc = MagicMock()
    fake_proc.returncode = 0
    fake_proc.stdout = "Filesystem Size Used Avail Use% Mounted on\n/dev/sda1 100G 42G 58G 42% /\n"
    mock_subproc.return_value = fake_proc
    
    assert check_disk_is_critical("/") is False

@patch("requests.post")
def test_query_slack_webhook_success(mock_post):
    fake_res = MagicMock()
    fake_res.status_code = 200
    mock_post.return_value = fake_res
    
    assert query_slack_webhook_alert("https://hooks.slack.com/fake", "Alert Test") is True
    # Verify exact payload passed to requests.post
    mock_post.assert_called_once_with(
        "https://hooks.slack.com/fake",
        json={"text": "Alert Test"},
        timeout=3
    )

if __name__ == "__main__":
    print("========================================")
    print("      MOCKING & UNIT TEST EXECUTION     ")
    print("========================================")
    test_check_disk_critical_true()
    print("[PASS] test_check_disk_critical_true (Mocked Subprocess)")
    test_check_disk_healthy()
    print("[PASS] test_check_disk_healthy (Mocked Subprocess)")
    test_query_slack_webhook_success()
    print("[PASS] test_query_slack_webhook_success (Mocked Requests)")
    print("----------------------------------------")
    print("[+] All mocked unit tests passed without touching OS or network!")
    print("========================================")
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
      MOCKING & UNIT TEST EXECUTION     
========================================
[PASS] test_check_disk_critical_true (Mocked Subprocess)
[PASS] test_check_disk_healthy (Mocked Subprocess)
[PASS] test_query_slack_webhook_success (Mocked Requests)
----------------------------------------
[+] All mocked unit tests passed without touching OS or network!
========================================
```

---

## 🔍 Line-by-line explanation
- `@patch("subprocess.run")`: Replaces `subprocess.run` with a `MagicMock` for the duration of the test.
- `mock_post.assert_called_once_with(...)`: Verifies not just the return value, but that the code called the API with the exact expected payload and timeout parameters.

---

## 🐚 Shell equivalent

Shell has no native mocking library; testing requires complex local fake binaries or wrappers.

---

## ⚙️ Ansible equivalent

Ansible playbooks are tested in isolated Docker containers via `molecule`.

---

## 🏆 Which one should I use?
- Use **`unittest.mock`** in Python to test API integrations, cloud resource calculations, and command executions reliably in hermetic CI runners without needing AWS credentials or live servers.

---

## ⚠️ Common mistakes
1. **Patching the wrong module path:**
   - Always patch where the object is *imported*, not where it is defined (`@patch("my_script.requests.get")` vs `@patch("requests.get")`).

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Write a unit test using `@patch("requests.get")` to verify that a health check function returns `False` when the remote endpoint returns HTTP `503 Service Unavailable`.

---

## 💡 Hint
Set `mock_get.return_value.status_code = 503`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "Why is mocking essential when writing unit tests for cloud automation scripts in CI/CD pipelines?"
> **Interviewer Focus:** Testing your understanding of hermetic test environments, isolation, avoiding cloud costs/side-effects, and deterministic builds.

---

## 🗣️ How to answer in an interview
> *"Unit tests must be fast, deterministic, and isolated (hermetic). In CI/CD runners, tests should not require live cloud credentials, internet connectivity, or risk executing destructive actions (like deleting cloud disks or terminating nodes). Mocking with `unittest.mock.patch` allows us to simulate every cloud API response, error code (`429`, `503`), and network timeout in memory, validating our failure handling logic without spending money or altering real infrastructure."*

---

## 📝 What I should remember
- Use `@patch("module.function")`.
- Use `MagicMock` to simulate response objects and methods.
- Use `mock.assert_called_once_with()` to verify outbound API payloads.
