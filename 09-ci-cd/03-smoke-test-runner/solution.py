"""
Lesson 03 (Module 09): Solution — Multi-Endpoint Smoke Verifier
"""
import requests
from typing import List

def verify_endpoints(endpoints_list: List[str]) -> bool:
    print("========================================")
    print("     CANARY SMOKE TEST VERIFICATION     ")
    print("========================================")
    
    all_healthy = True
    for url in endpoints_list:
        try:
            res = requests.get(url, timeout=3.0)
            if res.status_code == 200:
                print(f"[PASS] HTTP {res.status_code} -> {url}")
            else:
                print(f"[FAIL] HTTP {res.status_code} -> {url}")
                all_healthy = False
        except requests.exceptions.RequestException as err:
            print(f"[FAIL] Error: {err} -> {url}")
            all_healthy = False
            
    print("========================================")
    print(f"Overall Smoke Status: {'PASSED' if all_healthy else 'FAILED'}")
    print("========================================")
    return all_healthy

if __name__ == "__main__":
    test_urls = [
        "https://httpbin.org/status/200",
        "https://httpbin.org/json"
    ]
    verify_endpoints(test_urls)
