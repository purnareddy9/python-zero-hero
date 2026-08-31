"""
Lesson 03 (Module 10): Mocking External APIs, Subprocesses, and Cloud SDKs
Example Script: Unit Testing with Mocked Subprocesses and HTTP APIs
"""
import subprocess
import requests
from unittest.mock import patch, MagicMock

def check_disk_is_critical(mount_point="/"):
    proc = subprocess.run(["df", "-h", mount_point], capture_output=True, text=True)
    lines = proc.stdout.strip().split("\n")
    if len(lines) < 2:
        return False
    usage_str = lines[1].split()[4].replace("%", "")
    return int(usage_str) >= 85

def query_slack_webhook_alert(webhook_url, message):
    payload = {"text": message}
    res = requests.post(webhook_url, json=payload, timeout=3)
    return res.status_code == 200

@patch("subprocess.run")
def test_check_disk_critical_true(mock_subproc):
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
