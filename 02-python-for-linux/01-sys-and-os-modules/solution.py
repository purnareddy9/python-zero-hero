"""
Lesson 01 (Module 02): Solution — Log File Directory Auditor
"""
import sys
import os

def audit_log_files(target_dir):
    print("========================================")
    print("       LOG FILE DIRECTORY AUDIT         ")
    print("========================================")
    print(f"Target Directory: {os.path.abspath(target_dir)}\n")
    
    try:
        entries = os.listdir(target_dir)
    except PermissionError:
        print(f"[!] PERMISSION DENIED: Cannot read '{target_dir}'.")
        sys.exit(1)
        
    log_files = [f for f in entries if f.endswith(".log") and os.path.isfile(os.path.join(target_dir, f))]
    
    if not log_files:
        print("[*] No log files (.log) detected in directory.")
        print("========================================")
        sys.exit(0)
        
    total_size_kb = 0.0
    print("Detected Log Files:")
    for filename in sorted(log_files):
        full_path = os.path.join(target_dir, filename)
        size_kb = round(os.path.getsize(full_path) / 1024, 2)
        total_size_kb += size_kb
        print(f"  - {filename:<25} : {size_kb:>8.2f} KB")
        
    print("----------------------------------------")
    print(f"Total Logs: {len(log_files)} | Combined Size: {total_size_kb:.2f} KB")
    print("========================================")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Target directory argument required.")
        print("Usage: python solution.py <dir_path>")
        sys.exit(2)
        
    dir_path = sys.argv[1]
    if not os.path.exists(dir_path):
        print(f"Error: Directory '{dir_path}' not found.")
        sys.exit(1)
        
    if not os.path.isdir(dir_path):
        print(f"Error: Path '{dir_path}' is not a directory.")
        sys.exit(1)
        
    audit_log_files(dir_path)
