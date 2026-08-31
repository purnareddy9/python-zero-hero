"""
Lesson 03 (Module 03): JSON Processing
Example Script: Docker Inspect Parser & Vulnerability Scanner JSON Aggregator
"""
import json

mock_scan_report = """
{
  "image": "myregistry.io/payment-api:v2.1.0",
  "scan_time": "2026-08-31T10:15:00Z",
  "vulnerabilities": [
    {"cve": "CVE-2026-1001", "severity": "HIGH", "package": "openssl"},
    {"cve": "CVE-2026-1002", "severity": "LOW", "package": "curl"},
    {"cve": "CVE-2026-1003", "severity": "CRITICAL", "package": "glibc"}
  ]
}
"""

def parse_security_scan(raw_json_str):
    print("========================================")
    print("     CONTAINER SECURITY AUDIT REPORT    ")
    print("========================================")
    
    data = json.loads(raw_json_str)
    
    image = data.get("image")
    vulns = data.get("vulnerabilities", [])
    
    print(f"Target Image: {image}")
    print(f"Total CVEs  : {len(vulns)}\n")
    
    critical_cves = [v for v in vulns if v.get("severity") == "CRITICAL"]
    high_cves = [v for v in vulns if v.get("severity") == "HIGH"]
    
    print(f"Critical Severity: {len(critical_cves)}")
    print(f"High Severity    : {len(high_cves)}")
    print("----------------------------------------")
    
    if critical_cves:
        print("[!] BLOCKING DEPLOYMENT: Critical CVEs detected:")
        for cve in critical_cves:
            print(f"    - {cve['cve']} in package '{cve['package']}'")
        return False
        
    print("[+] Security gate passed. No critical vulnerabilities.")
    return True

if __name__ == "__main__":
    passed = parse_security_scan(mock_scan_report)
    print("========================================")
