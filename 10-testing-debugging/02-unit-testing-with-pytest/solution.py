"""
Lesson 02 (Module 10): Solution — Pytest IPv4 Address Validator Test Suite
"""
import pytest

def is_valid_ipv4(ip_str: str) -> bool:
    if not ip_str or not isinstance(ip_str, str):
        return False
    parts = ip_str.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        val = int(p)
        if not (0 <= val <= 255):
            return False
    return True

def test_valid_ipv4_addresses():
    valid_samples = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.254.1",
        "8.8.8.8",
        "0.0.0.0",
        "255.255.255.255"
    ]
    for ip in valid_samples:
        assert is_valid_ipv4(ip) is True, f"Failed for valid IP: {ip}"

def test_invalid_ipv4_addresses():
    invalid_samples = [
        "256.0.0.1",
        "192.168.1",
        "192.168.1.1.5",
        "abc.def.ghi.jkl",
        "192.168.1.-1",
        "",
        None,
        12345
    ]
    for ip in invalid_samples:
        assert is_valid_ipv4(ip) is False, f"Failed to reject invalid IP: {ip}"

if __name__ == "__main__":
    print("========================================")
    print("      PYTEST TEST SUITE EXECUTION       ")
    print("========================================")
    test_valid_ipv4_addresses()
    print("[PASS] test_valid_ipv4_addresses")
    test_invalid_ipv4_addresses()
    print("[PASS] test_invalid_ipv4_addresses")
    print("----------------------------------------")
    print("[+] All IPv4 test assertions passed!")
    print("========================================")
