"""
Lesson 00: Shell vs Python vs Ansible
Example Script: Memory Health Check & Webhook Payload Generator
"""
import sys
import platform

def check_memory_threshold(free_percent=12.5, threshold=15.0):
    server = platform.node() or "localhost"
    print("========================================")
    print("       SYSTEM MEMORY AUDIT CHECK        ")
    print("========================================")
    print(f"[*] Auditing host: {server}")
    print(f"[*] Free Memory: {free_percent}% (Threshold: {threshold}%)")
    
    if free_percent < threshold:
        alert_payload = {
            "server": server,
            "metric": "memory",
            "free_percent": free_percent,
            "status": "CRITICAL",
            "action_required": "Investigate high memory usage immediately"
        }
        print(f"\n[!] ALERT TRIGGERED:")
        print(f"    Payload: {alert_payload}")
        print("========================================")
        return False
    
    print("\n[+] System memory is healthy.")
    print("========================================")
    return True

if __name__ == "__main__":
    # Simulate a check where free memory is 12.5% (triggers alert)
    is_healthy = check_memory_threshold(free_percent=12.5, threshold=15.0)
    
    # Exit with code 1 on failure so CI/CD or orchestrators detect it
    if not is_healthy:
        sys.exit(1)
    sys.exit(0)
