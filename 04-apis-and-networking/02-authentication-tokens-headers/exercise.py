"""
Lesson 02 (Module 04): Exercise — Secure API Header Builder

Task:
Write a function `query_authenticated_api(endpoint_url: str, token_env_var: str = "SERVICE_API_KEY")`:
1. Reads the API token from `os.environ.get(token_env_var)`.
2. If token is missing, raise a `ValueError("Missing API key in environment")`.
3. Sets headers:
   `{"Authorization": f"Bearer {token}", "User-Agent": "DevOps-Deployer/2.0", "Accept": "application/json"}`
4. Sends GET request with 5-second timeout.
5. Returns `(response.status_code, response.headers.get("Content-Type"))`.
"""
import os
import requests

# TODO: Implement query_authenticated_api

if __name__ == "__main__":
    pass
