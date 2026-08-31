"""
Lesson 01 (Module 03): Solution — Audit Logger
"""
import time
import os

def append_audit_log(filepath: str, user: str, action: str, status: str = "SUCCESS") -> bool:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] USER: {user:<15} | ACTION: {action:<20} | STATUS: {status}\n"
    
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(log_line)
        return True
    except PermissionError:
        print(f"[!] PERMISSION DENIED: Cannot write to '{filepath}'")
        return False

if __name__ == "__main__":
    audit_file = "security_audit.log"
    print("========================================")
    print("        AUDIT LOGGER EXECUTION          ")
    print("========================================")
    
    append_audit_log(audit_file, "admin-sri", "DEPLOY_APP_V2", "SUCCESS")
    append_audit_log(audit_file, "ci-runner-04", "RUN_INTEGRATION_TESTS", "SUCCESS")
    append_audit_log(audit_file, "unknown-svc", "DATABASE_MIGRATE", "FAILED")
    
    print(f"[+] Successfully appended events to '{audit_file}'.")
    print("\nFile Contents:")
    with open(audit_file, "r", encoding="utf-8") as f:
        print(f.read())
    print("========================================")
