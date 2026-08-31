"""
Lesson 08: Solution — CPU Load Normalizer & Alert Function
"""
from typing import Dict, Any

def evaluate_cpu_load(hostname: str, load_avg_15m: float, core_count: int = 4) -> Dict[str, Any]:
    """
    Computes normalized CPU load per core and assigns operational health status.
    """
    if core_count <= 0:
        raise ValueError("core_count must be a positive integer greater than 0")
        
    normalized = round(load_avg_15m / core_count, 2)
    
    if normalized >= 1.0:
        status = "CRITICAL"
        is_overloaded = True
    elif normalized >= 0.7:
        status = "ELEVATED"
        is_overloaded = False
    else:
        status = "NORMAL"
        is_overloaded = False
        
    return {
        "hostname": hostname,
        "normalized_load": normalized,
        "is_overloaded": is_overloaded,
        "status": status
    }

if __name__ == "__main__":
    print("========================================")
    print("      CPU LOAD NORMALIZATION AUDIT      ")
    print("========================================")
    
    test_hosts = [
        ("web-prod-01", 2.5, 4),
        ("db-primary-01", 5.2, 4),
        ("worker-heavy-01", 6.0, 8)
    ]
    
    for host, load, cores in test_hosts:
        result = evaluate_cpu_load(host, load, cores)
        tag = f"[{result['status']}]"
        print(f"{tag:<10} Host: {result['hostname']:<16} | Load/Core: {result['normalized_load']} | Overloaded: {result['is_overloaded']}")
        
    print("========================================")
