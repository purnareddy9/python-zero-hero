"""
Capstone Module: Log Analysis & Diagnostics
"""
from collections import Counter
import os

def run_log_analysis(filepath="sample.log", top_n=3):
    print("=========================================")
    print("         LOG INCIDENT ANALYZER           ")
    print("=========================================")
    
    if not os.path.exists(filepath):
        # Create a mock sample log if not present
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("2026-08-31 [INFO] Service started\n")
            f.write("2026-08-31 [ERROR] DB_TIMEOUT: Connection dropped\n")
            f.write("2026-08-31 [ERROR] DB_TIMEOUT: Connection dropped\n")
            f.write("2026-08-31 [WARN] High memory\n")
            f.write("2026-08-31 [ERROR] AUTH_FAILURE: Invalid JWT\n")
            
    level_counts = Counter()
    error_reasons = Counter()
    total_lines = 0
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            if "[INFO]" in line:
                level_counts["INFO"] += 1
            elif "[WARN]" in line:
                level_counts["WARN"] += 1
            elif "[ERROR]" in line:
                level_counts["ERROR"] += 1
                reason = line.split("[ERROR]")[1].strip().split(":")[0]
                error_reasons[reason] += 1
                
    print(f"Target Log File : {filepath}")
    print(f"Total Lines     : {total_lines}")
    print(f"Error Count     : {level_counts['ERROR']}\n")
    
    print("Top Failure Categories:")
    for r, count in error_reasons.most_common(top_n):
        print(f"  - {r:<25} : {count} hit(s)")
    print("=========================================")
