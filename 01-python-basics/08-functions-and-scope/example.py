"""
Lesson 08: Functions, Scope, and Modularity
Example Script: Modular Server Health Audit Toolkit
"""
from typing import Dict, Tuple

def audit_service(name: str, port: int, response_code: int) -> Tuple[bool, str]:
    """
    Audits a microservice based on response code and port binding.
    Returns a tuple of (is_healthy, status_message).
    """
    if response_code == 200:
        return True, f"Service '{name}' on port {port} is operational."
    elif 500 <= response_code <= 599:
        return False, f"Service '{name}' failed with Server Error (HTTP {response_code})."
    else:
        return False, f"Service '{name}' returned unexpected status (HTTP {response_code})."

def run_fleet_audit(service_inventory: Dict[str, Dict[str, int]]) -> int:
    """
    Runs audit over entire service inventory and returns count of failing services.
    """
    print("========================================")
    print("      FLEET MICROSERVICE HEALTH         ")
    print("========================================")
    
    failures = 0
    for svc_name, meta in service_inventory.items():
        healthy, message = audit_service(
            name=svc_name,
            port=meta["port"],
            response_code=meta["code"]
        )
        tag = "[PASS]" if healthy else "[FAIL]"
        print(f"{tag:<7} {message}")
        if not healthy:
            failures += 1
            
    print("========================================")
    print(f"Audit Summary: {len(service_inventory) - failures} Healthy, {failures} Failed")
    print("========================================")
    return failures

if __name__ == "__main__":
    inventory = {
        "auth-api": {"port": 8081, "code": 200},
        "order-api": {"port": 8082, "code": 502},
        "billing-worker": {"port": 8083, "code": 200}
    }
    
    failed_count = run_fleet_audit(inventory)
