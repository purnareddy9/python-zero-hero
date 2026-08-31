"""
Lesson 02 (Module 07): Solution — Deployment Rollout Validator
"""
from typing import Dict, Any, Tuple

def validate_deployment_health(deployment_data: Dict[str, Any]) -> Tuple[bool, str, int]:
    spec = deployment_data.get("spec", {})
    status = deployment_data.get("status", {})
    
    desired = spec.get("replicas", 1)
    available = status.get("available_replicas", 0)
    
    missing = max(0, desired - available)
    is_healthy = (available == desired) and (missing == 0)
    
    state_label = "HEALTHY" if is_healthy else "DEGRADED"
    return is_healthy, state_label, missing

if __name__ == "__main__":
    test_cases = [
        {"name": "auth-api", "spec": {"replicas": 3}, "status": {"available_replicas": 3}},
        {"name": "payment-worker", "spec": {"replicas": 5}, "status": {"available_replicas": 2}},
        {"name": "frontend-web", "spec": {"replicas": 4}, "status": {"available_replicas": 4}}
    ]
    
    print("========================================")
    print("     K8S ROLLOUT INTEGRITY AUDITOR      ")
    print("========================================")
    for test in test_cases:
        healthy, state, missing_count = validate_deployment_health(test)
        tag = f"[{state}]"
        print(f"{tag:<10} Deployment: {test['name']:<18} | Desired: {test['spec']['replicas']} | Missing: {missing_count}")
    print("========================================")
