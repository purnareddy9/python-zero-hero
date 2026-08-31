"""
Lesson 06: Solution — Security Incident IP Auditor
"""

access_log_ips = [
    "192.168.1.10",
    "10.0.0.1",
    "192.168.1.10",
    "45.33.32.156",
    "10.0.0.1",
    "198.51.100.4",
    "192.168.1.10"
]

known_malicious_ips = {"45.33.32.156", "203.0.113.5", "198.51.100.4"}

# 1. Deduplicate IPs
unique_ips = set(access_log_ips)

# 2. Set intersection to find blacklisted IPs in logs
flagged_threats = unique_ips & known_malicious_ips

# 3. Frequency count using a dictionary
ip_frequency = {}
for ip in access_log_ips:
    ip_frequency[ip] = ip_frequency.get(ip, 0) + 1

# 4. Print Security Report
print("========================================")
print("     SECURITY INCIDENT AUDIT REPORT     ")
print("========================================")
print(f"Total Log Events    : {len(access_log_ips)}")
print(f"Unique Visitor IPs  : {len(unique_ips)}")
print(f"Malicious Hits Found: {len(flagged_threats)}\n")

print("Traffic Frequency Breakdown:")
for ip, count in ip_frequency.items():
    threat_tag = " [!] THREAT" if ip in flagged_threats else ""
    print(f"  {ip:<16} : {count} request(s){threat_tag}")

print("========================================")
