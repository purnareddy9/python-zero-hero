"""
Lesson 03 (Module 07): Solution — Container Exit Code Diagnostic Engine
"""
from typing import Dict, Any

def diagnose_container_exit(exit_code: int) -> Dict[str, Any]:
    if exit_code == 0:
        return {
            "exit_code": exit_code,
            "severity": "INFO",
            "diagnosis": "Graceful process completion",
            "recommended_action": "None required"
        }
    elif exit_code in [1, 2]:
        return {
            "exit_code": exit_code,
            "severity": "CRITICAL",
            "diagnosis": "Application crash / unhandled exception",
            "recommended_action": "Check application stack trace logs"
        }
    elif exit_code == 137:
        return {
            "exit_code": exit_code,
            "severity": "CRITICAL",
            "diagnosis": "OOMKilled (Out of Memory - SIGKILL 9)",
            "recommended_action": "Increase container resources.limits.memory in pod spec"
        }
    elif exit_code == 143:
        return {
            "exit_code": exit_code,
            "severity": "WARNING",
            "diagnosis": "Graceful SIGTERM received (K8s pod eviction or scale down)",
            "recommended_action": "Verify if scale-down was expected"
        }
    else:
        return {
            "exit_code": exit_code,
            "severity": "WARNING",
            "diagnosis": f"Non-standard exit code ({exit_code})",
            "recommended_action": "Inspect container stderr logs for details"
        }

if __name__ == "__main__":
    test_codes = [0, 1, 137, 143, 255]
    print("========================================")
    print("     CONTAINER EXIT CODE DIAGNOSTICS    ")
    print("========================================")
    for code in test_codes:
        diag = diagnose_container_exit(code)
        tag = f"[{diag['severity']}]"
        print(f"{tag:<10} Exit Code {diag['exit_code']:<3} -> {diag['diagnosis']}")
        print(f"           Action: {diag['recommended_action']}\n")
    print("========================================")
