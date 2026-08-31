"""
Lesson 02 (Module 10): Unit Testing DevOps Scripts with pytest
Example Script: Verification for Core Infrastructure Utilities
"""
import re
import math

def calculate_required_nodes(total_workload_ram_gb: float, ram_per_node_gb: float = 16.0) -> int:
    if total_workload_ram_gb <= 0:
        return 0
    return math.ceil(total_workload_ram_gb / ram_per_node_gb)

def sanitize_docker_tag(branch_name: str) -> str:
    sanitized = branch_name.lower().replace("/", "-").replace("_", "-")
    return re.sub(r"[^a-z0-9.-]", "", sanitized)

def test_node_capacity_calculation():
    assert calculate_required_nodes(30.0, 16.0) == 2
    assert calculate_required_nodes(34.0, 16.0) == 3
    assert calculate_required_nodes(0.0, 16.0) == 0

def test_docker_tag_sanitization():
    assert sanitize_docker_tag("feature/user-auth") == "feature-user-auth"
    assert sanitize_docker_tag("BUGFIX/Fix_Issue#123") == "bugfix-fix-issue123"
    assert sanitize_docker_tag("release/v2.0.0") == "release-v2.0.0"

if __name__ == "__main__":
    print("========================================")
    print("      RUNNING MANUAL TEST RUNNER        ")
    print("========================================")
    test_node_capacity_calculation()
    print("[PASS] test_node_capacity_calculation")
    test_docker_tag_sanitization()
    print("[PASS] test_docker_tag_sanitization")
    print("----------------------------------------")
    print("[+] All unit tests executed successfully!")
    print("========================================")
