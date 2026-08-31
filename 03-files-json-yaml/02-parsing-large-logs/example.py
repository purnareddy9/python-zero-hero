"""
Lesson 02 (Module 03): Parsing Large Log Files Without Crashing Memory
Example Script: High-Performance Streaming Log Analyzer
"""
from collections import Counter
import os

def generate_mock_log(filename="production_access.log", count=600):
    """Generates sample access log entries for demonstration."""
    sample_templates = [
        "2026-08-31 10:01:02 [INFO] GET /api/v1/users 200 12ms",
        "2026-08-31 10:01:05 [INFO] POST /api/v1/checkout 201 45ms",
        "2026-08-31 10:01:10 [WARN] GET /api/v1/products 404 8ms",
        "2026-08-31 10:01:14 [ERROR] POST /api/v1/payment 500 DB_CONNECTION_TIMEOUT",
        "2026-08-31 10:01:18 [ERROR] GET /api/v1/orders 503 SERVICE_UNAVAILABLE",
        "2026-08-31 10:01:22 [ERROR] POST /api/v1/payment 500 DB_CONNECTION_TIMEOUT"
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(count):
            f.write(sample_templates[i % len(sample_templates)] + "\n")

def stream_analyze_log(filepath):
    print("========================================")
    print("      STREAMING LOG FILE ANALYZER       ")
    print("========================================")
    print(f"Analyzing: {os.path.abspath(filepath)}")
    
    total_lines = 0
    level_counts = Counter()
    error_reasons = Counter()
    
    # Stream line by line (O(1) memory consumption)
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            line = line.strip()
            
            # Extract log level
            if "[INFO]" in line:
                level_counts["INFO"] += 1
            elif "[WARN]" in line:
                level_counts["WARN"] += 1
            elif "[ERROR]" in line:
                level_counts["ERROR"] += 1
                parts = line.split(" ")
                if len(parts) >= 6:
                    error_reasons[parts[-1]] += 1
                    
    print(f"Total Lines Processed : {total_lines}")
    print("----------------------------------------")
    print("Log Level Breakdown:")
    for level, count in level_counts.items():
        pct = round((count / total_lines) * 100, 2)
        print(f"  - {level:<6} : {count:>5} ({pct}%)")
        
    print("----------------------------------------")
    print("Top Error Root Causes:")
    for reason, count in error_reasons.most_common(3):
        print(f"  - {reason:<25} : {count} occurrences")
        
    print("========================================")

if __name__ == "__main__":
    log_file = "production_access.log"
    generate_mock_log(log_file, count=600)
    stream_analyze_log(log_file)
