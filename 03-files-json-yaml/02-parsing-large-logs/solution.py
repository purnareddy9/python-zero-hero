"""
Lesson 02 (Module 03): Solution — Error Rate Calculator
"""
import os
from typing import Tuple

def calculate_error_rate(log_filepath: str, max_allowed_error_pct: float = 5.0) -> Tuple[bool, float]:
    if not os.path.exists(log_filepath):
        raise FileNotFoundError(f"Log file '{log_filepath}' not found.")
        
    total_lines = 0
    error_lines = 0
    
    with open(log_filepath, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            if "ERROR" in line or "CRITICAL" in line:
                error_lines += 1
                
    if total_lines == 0:
        return True, 0.0
        
    error_pct = round((error_lines / total_lines) * 100, 2)
    is_healthy = error_pct <= max_allowed_error_pct
    return is_healthy, error_pct

if __name__ == "__main__":
    test_file = "service_canary.log"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("2026-08-31 INFO starting\n")
        f.write("2026-08-31 INFO probe ok\n")
        f.write("2026-08-31 ERROR connection dropped\n")
        f.write("2026-08-31 INFO probe ok\n")
        f.write("2026-08-31 INFO probe ok\n")
        
    healthy, rate = calculate_error_rate(test_file, max_allowed_error_pct=10.0)
    print("========================================")
    print("       CANARY ERROR RATE EVALUATION     ")
    print("========================================")
    print(f"Calculated Error Rate : {rate}%")
    print(f"Meets SLO (<= 10.0%)  : {healthy}")
    if not healthy:
        print("[!] ROLLBACK REQUIRED: Error budget exceeded.")
    else:
        print("[+] SLO Satisfied. Deployment stable.")
    print("========================================")
