"""
Lesson 02 (Module 04): Authentication, Tokens, and Custom Headers
Example Script: GitHub Release & Pull Request Audit Client
"""
import requests
import os

def fetch_github_repo_info(owner="kubernetes", repo="kubernetes"):
    print("========================================")
    print("       GITHUB REPO RELEASE AUDITOR      ")
    print("========================================")
    
    token = os.environ.get("GITHUB_TOKEN")
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "DevOps-Audit-Script/1.0"
    }
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
        print("[*] Authenticating with provided GITHUB_TOKEN.")
    else:
        print("[*] Running unauthenticated (subject to lower public rate limits).")
        
    try:
        response = requests.get(api_url, headers=headers, timeout=5)
        rate_remaining = response.headers.get("X-RateLimit-Remaining", "N/A")
        print(f"API Rate Limit Remaining: {rate_remaining}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Repository   : {data['full_name']}")
            print(f"Description  : {data['description']}")
            print(f"Stars Count  : {data['stargazers_count']}")
            print(f"Open Issues  : {data['open_issues_count']}")
            print(f"Default Branch: {data['default_branch']}")
            return True
        elif response.status_code == 401:
            print("[!] AUTHENTICATION ERROR: Invalid or expired GitHub token.")
            return False
        elif response.status_code == 403:
            print("[!] RATE LIMIT REACHED: GitHub API rate limit exceeded.")
            return False
        else:
            print(f"[!] API Error: Received HTTP {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as err:
        print(f"[!] Network Error: {err}")
        return False
        
    print("========================================")

if __name__ == "__main__":
    fetch_github_repo_info("torvalds", "linux")
