"""
Lesson 02 (Module 04): Solution — Secure API Header Builder
"""
import os
import requests
from typing import Tuple

def query_authenticated_api(endpoint_url: str, token_env_var: str = "SERVICE_API_KEY") -> Tuple[int, str]:
    token = os.environ.get(token_env_var)
    if not token:
        raise ValueError(f"Missing API key in environment variable '{token_env_var}'")
        
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "DevOps-Deployer/2.0",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(endpoint_url, headers=headers, timeout=5)
        content_type = response.headers.get("Content-Type", "unknown")
        return response.status_code, content_type
    except requests.exceptions.RequestException as err:
        print(f"[!] Request failed: {err}")
        return 0, "ERROR"

if __name__ == "__main__":
    print("========================================")
    print("      AUTHENTICATED HEADER AUDIT        ")
    print("========================================")
    
    # Simulate setting token in environment
    os.environ["SERVICE_API_KEY"] = "sec_prod_token_991823"
    
    status, c_type = query_authenticated_api("https://httpbin.org/bearer")
    print(f"Response Status      : {status}")
    print(f"Response Content-Type: {c_type}")
    print("========================================")
