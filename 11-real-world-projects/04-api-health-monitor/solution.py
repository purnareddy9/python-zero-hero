"""
Project 04: Solution — SLA CSV Reporter
"""
import requests
import time
import csv
import os

TARGET_ENDPOINTS = [
    {"service": "Authentication API", "url": "https://httpbin.org/status/200", "sla_ms": 1000},
    {"service": "User Profile Service", "url": "https://httpbin.org/json", "sla_ms": 1500}
]

def run_and_export_probes(endpoints=TARGET_ENDPOINTS, output_csv="api_sla_audit.csv"):
    results = []
    for ep in endpoints:
        start = time.time()
        try:
            res = requests.get(ep["url"], timeout=3.0)
            lat = round((time.time() - start) * 1000, 2)
            ok = (res.status_code == 200) and (lat <= ep["sla_ms"])
            results.append({
                "service": ep["service"],
                "url": ep["url"],
                "status": f"HTTP_{res.status_code}",
                "latency_ms": lat,
                "is_ok": ok
            })
        except requests.exceptions.RequestException:
            results.append({
                "service": ep["service"],
                "url": ep["url"],
                "status": "UNREACHABLE",
                "latency_ms": 0.0,
                "is_ok": False
            })
            
    if results:
        fieldnames = ["service", "url", "status", "latency_ms", "is_ok"]
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
            
    print("=========================================")
    print("     API HEALTH AUDIT & CSV EXPORT       ")
    print("=========================================")
    print(f"[+] Exported {len(results)} probe records to '{os.path.abspath(output_csv)}'")
    print("=========================================")

if __name__ == "__main__":
    run_and_export_probes()
