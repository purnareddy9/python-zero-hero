"""
Lesson 03 (Module 09): Post-Deployment Smoke Test Runner & Automated Rollback
Example Script: CI/CD Post-Deployment Smoke Test Suite & Gatekeeper
"""
import requests
import time
import sys

SMOKE_TEST_SUITE = [
    {
        "name": "Health Status Probe",
        "url": "https://httpbin.org/status/200",
        "expected_status": 200,
        "max_latency_ms": 1500
    },
    {
        "name": "JSON API Schema Validation",
        "url": "https://httpbin.org/json",
        "expected_status": 200,
        "max_latency_ms": 2000,
        "required_json_keys": ["slideshow"]
    }
]

def run_post_deploy_smoke_tests(tests=SMOKE_TEST_SUITE):
    print("========================================")
    print("     POST-DEPLOYMENT SMOKE TEST RUNNER  ")
    print("========================================")
    
    passed_tests = 0
    failed_tests = []
    
    for test in tests:
        name = test["name"]
        url = test["url"]
        expected_code = test["expected_status"]
        max_latency = test["max_latency_ms"]
        
        print(f"[*] Running: {name:<30} -> {url}")
        start = time.time()
        
        try:
            res = requests.get(url, timeout=4.0)
            latency = round((time.time() - start) * 1000, 2)
            
            if res.status_code != expected_code:
                failed_tests.append((name, f"Expected HTTP {expected_code}, received {res.status_code}"))
                print(f"    [FAIL] Status Code mismatch (HTTP {res.status_code})")
                continue
                
            if latency > max_latency:
                failed_tests.append((name, f"Latency breached SLO: {latency}ms > {max_latency}ms"))
                print(f"    [FAIL] Latency breach ({latency} ms)")
                continue
                
            if "required_json_keys" in test:
                body = res.json()
                for key in test["required_json_keys"]:
                    if key not in body:
                        failed_tests.append((name, f"Missing required JSON key '{key}'"))
                        print(f"    [FAIL] Missing schema key '{key}'")
                        continue
                        
            print(f"    [PASS] (Status: {res.status_code}, Latency: {latency} ms)")
            passed_tests += 1
            
        except Exception as err:
            failed_tests.append((name, f"Network exception: {err}"))
            print(f"    [FAIL] Exception: {err}")
            
    print("========================================")
    print(f"Smoke Test Summary: {passed_tests}/{len(tests)} Passed")
    
    if failed_tests:
        print("\n[!] CRITICAL DEPLOYMENT FAILURE: Rollback recommended!")
        for name, reason in failed_tests:
            print(f"    - {name}: {reason}")
        print("========================================")
        return False
        
    print("[+] All smoke tests passed. Promotion approved.")
    print("========================================")
    return True

if __name__ == "__main__":
    success = run_post_deploy_smoke_tests()
    sys.exit(0 if success else 1)
