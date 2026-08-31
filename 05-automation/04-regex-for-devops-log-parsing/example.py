"""
Lesson 04 (Module 05): Regular Expressions (re) for DevOps Log Parsing
Example Script: Nginx Web Server Access Log RegEx Parser
"""
import re

nginx_log_samples = [
    '192.168.1.100 - - [31/Aug/2026:14:10:02 +0000] "GET /api/v1/health HTTP/1.1" 200 45 "-" "curl/7.68.0"',
    '10.0.5.22 - - [31/Aug/2026:14:10:05 +0000] "POST /api/v1/auth/login HTTP/1.1" 401 120 "-" "Mozilla/5.0"',
    '45.33.32.156 - - [31/Aug/2026:14:10:09 +0000] "GET /admin.php HTTP/1.1" 404 180 "-" "ScannerBot/2.0"',
    '192.168.1.105 - - [31/Aug/2026:14:10:14 +0000] "POST /api/v1/checkout HTTP/1.1" 500 512 "-" "AppClient/3.1"'
]

def parse_nginx_logs(logs):
    print("========================================")
    print("      REGEX NGINX ACCESS LOG AUDITOR    ")
    print("========================================")
    
    pattern = re.compile(
        r'^(?P<client_ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<endpoint>\S+)[^"]*"\s+(?P<status>\d{3})\s+(?P<bytes_sent>\d+)'
    )
    
    for line in logs:
        match = pattern.search(line)
        if match:
            ip = match.group("client_ip")
            method = match.group("method")
            endpoint = match.group("endpoint")
            status = int(match.group("status"))
            
            tag = "[ERROR]  " if status >= 400 else "[OK]     "
            print(f"{tag} IP: {ip:<15} | Status: {status} | Request: {method} {endpoint}")
            
    print("========================================")

if __name__ == "__main__":
    parse_nginx_logs(nginx_log_samples)
