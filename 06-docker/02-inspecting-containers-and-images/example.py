"""
Lesson 02 (Module 06): Inspecting Containers, Environment Variables, and Image Tags
Example Script: Container Governance & Security Policy Compliance Auditor
"""

def audit_container_security_spec(container_attrs):
    print("========================================")
    print("     CONTAINER SECURITY AUDIT SPEC      ")
    print("========================================")
    
    name = container_attrs.get("Name", "").lstrip("/")
    state = container_attrs.get("State", {})
    host_config = container_attrs.get("HostConfig", {})
    
    mem_bytes = host_config.get("Memory", 0)
    mem_mb = round(mem_bytes / (1024 ** 2), 2) if mem_bytes > 0 else "UNLIMITED (FAIL)"
    is_privileged = host_config.get("Privileged", False)
    readonly_root = host_config.get("ReadonlyRootfs", False)
    restart_policy = host_config.get("RestartPolicy", {}).get("Name", "no")
    
    print(f"Container Name   : {name}")
    print(f"Status           : {state.get('Status')}")
    print(f"Memory Limit     : {mem_mb} MB")
    print(f"Privileged Mode  : {is_privileged} (Expected: False)")
    print(f"Read-Only RootFS : {readonly_root}")
    print(f"Restart Policy   : {restart_policy}")
    print("----------------------------------------")
    
    violations = []
    if mem_bytes == 0:
        violations.append("Memory limit is not set (OOM / DoS vulnerability)")
    if is_privileged:
        violations.append("Container is running in PRIVILEGED mode (Root breakout risk)")
    if restart_policy == "no":
        violations.append("No automatic restart policy configured")
        
    if violations:
        print("[!] GOVERNANCE VIOLATIONS DETECTED:")
        for v in violations:
            print(f"    - {v}")
        return False
    else:
        print("[+] Container meets all security compliance policies.")
        return True

if __name__ == "__main__":
    mock_container_attrs = {
        "Name": "/payment-gateway-service",
        "State": {"Status": "running", "Running": True},
        "HostConfig": {
            "Memory": 536870912,
            "Privileged": False,
            "ReadonlyRootfs": True,
            "RestartPolicy": {"Name": "always"}
        },
        "Config": {"Image": "myregistry.io/payment:v2.0"}
    }
    
    audit_container_security_spec(mock_container_attrs)
