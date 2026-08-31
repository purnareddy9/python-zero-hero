r"""
Project 02: Exercise — IP-Aware Log Incident Parser

Task:
You are analyzing logs where error lines include IP addresses:
`"2026-08-31 10:01:15 [ERROR] [IP:192.168.1.50] DatabaseConnectionError"`

Write a function `extract_error_ips(filepath)`:
1. Streams `filepath` line by line.
2. Identifies lines containing `[ERROR]` or `[CRITICAL]`.
3. Extracts the IP address using regex `r"\[IP:(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\]"`.
4. Returns a dictionary mapping unique IPs to their error counts: `{"192.168.1.50": 5, ...}`.
"""

# TODO: Implement extract_error_ips function

if __name__ == "__main__":
    pass
