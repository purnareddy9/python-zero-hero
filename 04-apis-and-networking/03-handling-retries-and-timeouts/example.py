"""
Lesson 03 (Module 04): Handling Retries, Exponential Backoff, and Timeouts
Example Script: Resilient Cloud API Poller with Exponential Backoff
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import time

def get_resilient_session(max_retries=3, backoff=0.5):
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

def poll_microservice_readiness(url, max_attempts=3):
    print("========================================")
    print("     RESILIENT API POLLING SERVICE      ")
    print("========================================")
    
    session = get_resilient_session(max_retries=2, backoff=0.3)
    
    for attempt in range(1, max_attempts + 1):
        print(f"[*] [Probe {attempt}/{max_attempts}] Querying: {url}")
        try:
            response = session.get(url, timeout=(2.0, 5.0))
            print(f"    Response Status: HTTP {response.status_code}")
            
            if response.status_code == 200:
                print("[+] Service reached READY state.")
                return True
            else:
                print(f"    Service in degraded state (HTTP {response.status_code}).")
                
        except requests.exceptions.RequestException as err:
            print(f"    [!] Connection error: {err}")
            
        delay = 2 ** (attempt - 1)
        print(f"    Backing off for {delay} seconds...\n")
        time.sleep(delay)
        
    print("[!] TIMEOUT: Service failed readiness probes.")
    print("========================================")
    return False

if __name__ == "__main__":
    poll_microservice_readiness("https://httpbin.org/status/200", max_attempts=2)
