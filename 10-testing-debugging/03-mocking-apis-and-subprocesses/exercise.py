"""
Lesson 03 (Module 10): Exercise — Mocking Remote Cloud Health Check

Task:
You are given a function `probe_remote_status(api_url: str) -> bool`:
```python
def probe_remote_status(api_url: str) -> bool:
    try:
        res = requests.get(api_url, timeout=2)
        return res.status_code == 200
    except Exception:
        return False
```

Write two pytest unit tests using `@patch("requests.get")`:
1. `test_probe_remote_status_healthy(mock_get)`: Mock a return value with `status_code = 200` and assert the function returns `True`.
2. `test_probe_remote_status_503_error(mock_get)`: Mock a return value with `status_code = 503` and assert the function returns `False`.
"""
import requests
from unittest.mock import patch, MagicMock

def probe_remote_status(api_url: str) -> bool:
    try:
        res = requests.get(api_url, timeout=2)
        return res.status_code == 200
    except Exception:
        return False

# TODO: Write test_probe_remote_status_healthy and test_probe_remote_status_503_error

if __name__ == "__main__":
    pass
