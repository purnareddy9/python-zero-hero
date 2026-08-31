"""
Lesson 06: Exercise — Security Incident IP Auditor

Task:
You are analyzing an active web server access log.
`access_log_ips = ["192.168.1.10", "10.0.0.1", "192.168.1.10", "45.33.32.156", "10.0.0.1", "198.51.100.4", "192.168.1.10"]`
`known_malicious_ips = {"45.33.32.156", "203.0.113.5", "198.51.100.4"}`

Requirements:
1. Extract all unique IP addresses from `access_log_ips` using a set.
2. Find if any of the accessed IPs are in `known_malicious_ips` (set intersection).
3. Count how many times each IP appeared in the log using a dictionary frequency map.
4. Print a clean security report.
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

# TODO: Implement security audit using sets and dictionaries
