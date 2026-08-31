"""
Lesson 03 (Module 09): Exercise — Multi-Endpoint Smoke Verifier

Task:
Write a function `verify_endpoints(endpoints_list: list) -> bool`:
Given a list of URLs:
1. Loops through each URL.
2. Performs a GET request with `timeout=3.0`.
3. Validates that `status_code == 200`.
4. If any endpoint fails or throws an exception, print `[FAIL] <url>` and return `False`.
5. If all pass, print `[ALL PASS]` and return `True`.
"""
import requests

# TODO: Implement verify_endpoints function

if __name__ == "__main__":
    pass
