"""
Project 02: Solution — IP-Aware Log Incident Parser
"""
import re
from collections import Counter
from typing import Dict

IP_REGEX = re.compile(r"\[IP:(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\]")

def extract_error_ips(filepath: str) -> Dict[str, int]:
    ip_counter = Counter()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if "[ERROR]" in line or "[CRITICAL]" in line:
                match = IP_REGEX.search(line)
                if match:
                    ip = match.group("ip")
                    ip_counter[ip] += 1
    return dict(ip_counter)

if __name__ == "__main__":
    test_log = "ip_errors.log"
    with open(test_log, "w", encoding="utf-8") as f:
        f.write("2026-08-31 10:01:15 [ERROR] [IP:192.168.1.50] DB timeout\n")
        f.write("2026-08-31 10:01:18 [ERROR] [IP:10.0.0.5] Auth failed\n")
        f.write("2026-08-31 10:01:20 [ERROR] [IP:192.168.1.50] Connection dropped\n")
        f.write("2026-08-31 10:01:25 [INFO] [IP:192.168.1.100] User logged in\n")
        
    print("=========================================")
    print("      IP ERROR INCIDENT BREAKDOWN        ")
    print("=========================================")
    results = extract_error_ips(test_log)
    for ip, count in results.items():
        print(f"  - IP: {ip:<18} -> {count} error event(s)")
    print("=========================================")
