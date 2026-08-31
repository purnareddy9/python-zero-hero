"""
Lesson 03 (Module 10): Solution — Mocking Remote Cloud Health Check
"""
import requests
from unittest.mock import patch, MagicMock

def probe_remote_status(api_url: str) -> bool:
    try:
        res = requests.get(api_url, timeout=2)
        return res.status_code == 200
    except Exception:
        return False

@patch("requests.get")
def test_probe_remote_status_healthy(mock_get):
    fake_res = MagicMock()
    fake_res.status_code = 200
    mock_get.return_value = fake_res
    
    assert probe_remote_status("https://api.internal/health") is True
    mock_get.assert_called_once_with("https://api.internal/health", timeout=2)

@patch("requests.get")
def test_probe_remote_status_503_error(mock_get):
    fake_res = MagicMock()
    fake_res.status_code = 503
    mock_get.return_value = fake_res
    
    assert probe_remote_status("https://api.internal/health") is False

if __name__ == "__main__":
    print("========================================")
    print("      MOCKED API PROBE TEST EXECUTION   ")
    print("========================================")
    test_probe_remote_status_healthy()
    print("[PASS] test_probe_remote_status_healthy")
    test_probe_remote_status_503_error()
    print("[PASS] test_probe_remote_status_503_error")
    print("----------------------------------------")
    print("[+] All HTTP mock tests passed!")
    print("========================================")
