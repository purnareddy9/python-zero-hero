"""
Lesson 03 (Module 04): Solution — Backoff Retry Client
"""
import requests
import time
from typing import Tuple, Any

def fetch_with_backoff(url: str, max_retries: int = 3, base_delay: float = 0.5) -> Tuple[bool, Any]:
    print("========================================")
    print("      CUSTOM EXPONENTIAL BACKOFF CLIENT ")
    print("========================================")
    
    for attempt in range(1, max_retries + 1):
        print(f"[*] [Attempt {attempt}/{max_retries}] Requesting: {url}")
        try:
            response = requests.get(url, timeout=2.0)
            if response.status_code == 200:
                print("[+] Success on attempt", attempt)
                return True, response.json()
            elif response.status_code in [429, 500, 502, 503, 504]:
                print(f"    [!] Received HTTP {response.status_code} (Transient Error)")
            else:
                # Permanent failure (e.g. 404 Not Found, 401 Unauthorized) -> do not retry
                print(f"    [!] Non-retriable HTTP status {response.status_code}")
                return False, f"HTTP_{response.status_code}"
                
        except requests.exceptions.RequestException as err:
            print(f"    [!] Network exception encountered: {err}")
            
        if attempt < max_retries:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"    Backing off for {delay:.2f}s before retry...\n")
            time.sleep(delay)
            
    print("[!] Maximum retry threshold reached without success.")
    print("========================================")
    return False, "MAX_RETRIES_EXCEEDED"

if __name__ == "__main__":
    success, data = fetch_with_backoff("https://httpbin.org/json", max_retries=2)
    print(f"Result: Success = {success}")
