"""
Lesson 01 (Module 04): Solution — JSON API Consumer
"""
import requests
from typing import Tuple

def fetch_sample_json_title(api_url: str = "https://httpbin.org/json") -> Tuple[bool, str]:
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            title = data.get("slideshow", {}).get("title", "No Title Found")
            return True, title
        else:
            return False, f"HTTP Error: Received status code {response.status_code}"
    except requests.exceptions.Timeout:
        return False, "Request timed out after 5 seconds"
    except requests.exceptions.RequestException as err:
        return False, f"Network communication failed: {err}"

if __name__ == "__main__":
    print("========================================")
    print("      API DATA RETRIEVAL AUDIT          ")
    print("========================================")
    success, result = fetch_sample_json_title()
    if success:
        print(f"[+] Successfully extracted Title: '{result}'")
    else:
        print(f"[!] Extraction failed: {result}")
    print("========================================")
