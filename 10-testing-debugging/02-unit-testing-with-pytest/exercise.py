"""
Lesson 02 (Module 10): Exercise — Pytest IPv4 Address Validator Test Suite

Task:
You are given an IP validator function `is_valid_ipv4(ip_str: str) -> bool`.
Write two pytest test functions:
1. `test_valid_ipv4_addresses()`: Assert that standard valid IPs return True (`"192.168.1.1"`, `"10.0.0.1"`, `"8.8.8.8"`).
2. `test_invalid_ipv4_addresses()`: Assert that invalid inputs return False (`"256.0.0.1"`, `"1.2.3"`, `"abc.def.ghi.jkl"`, `""`, `None`).
"""

def is_valid_ipv4(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    parts = ip_str.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit() or not (0 <= int(p) <= 255):
            return False
    return True

# TODO: Write test_valid_ipv4_addresses and test_invalid_ipv4_addresses

if __name__ == "__main__":
    pass
