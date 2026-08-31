"""
Lesson 03 (Module 04): Exercise — Backoff Retry Client

Task:
Write a custom function `fetch_with_backoff(url: str, max_retries: int = 3, base_delay: float = 0.5)`:
1. Loops up to `max_retries` attempts.
2. Sends GET request with `timeout=2.0`.
3. If response status is 200, return `(True, response.json())`.
4. If response is 500, 502, 503, or a `requests.exceptions.RequestException` occurs:
   - Compute `sleep_time = base_delay * (2 ** (attempt - 1))`
   - Print retry notice and sleep.
5. If all retries fail, return `(False, "Exceeded max retry limit")`.
"""
import requests
import time

# TODO: Implement fetch_with_backoff function

if __name__ == "__main__":
    pass
