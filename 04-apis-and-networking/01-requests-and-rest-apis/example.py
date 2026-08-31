"""
Lesson 01 (Module 04): REST APIs and the requests Module
Example Script: Microservice Health Probe & Slack Alert Webhook Dispatcher
"""
import requests
import json
import time

def probe_health_endpoint(url, timeout_sec=3):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout_sec)
        latency_ms = round((time.time() - start_time) * 1000, 2)
        is_healthy = response.status_code == 200
        return is_healthy, latency_ms, response.status_code
    except requests.exceptions.Timeout:
        return False, timeout_sec * 1000, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return False, 0.0, "CONNECTION_REFUSED"

def send_mock_slack_alert(webhook_url, service_name, status_code, latency_ms):
    payload = {
        "text": f"🚨 *SERVICE OUTAGE ALERT*: `{service_name}` is DOWN!",
        "attachments": [
            {
                "color": "danger",
                "fields": [
                    {"title": "Service", "value": service_name, "short": True},
                    {"title": "Status Code", "value": str(status_code), "short": True},
                    {"title": "Probe Latency", "value": f"{latency_ms} ms", "short": True},
                    {"title": "Action", "value": "Traffic automatically routed away", "short": True}
                ]
            }
        ]
    }
    
    print(f"[*] Posting Webhook to Slack URL: {webhook_url}")
    print(f"    Payload: {json.dumps(payload, indent=2)}")
    return True

if __name__ == "__main__":
    print("========================================")
    print("      API PROBE & ALERT SYSTEM          ")
    print("========================================")
    
    test_endpoints = [
        ("Public JSON API", "https://httpbin.org/status/200"),
        ("Simulated 500 Error", "https://httpbin.org/status/500")
    ]
    
    for name, url in test_endpoints:
        print(f"[*] Probing {name} ({url})...")
        healthy, latency, code = probe_health_endpoint(url)
        
        if healthy:
            print(f"    [+] HEALTHY: HTTP {code} (Latency: {latency} ms)\n")
        else:
            print(f"    [!] UNHEALTHY: HTTP {code} (Latency: {latency} ms)")
            send_mock_slack_alert(
                webhook_url="https://hooks.slack.com/services/T00/B00/XXXX",
                service_name=name,
                status_code=code,
                latency_ms=latency
            )
            print()
            
    print("========================================")
