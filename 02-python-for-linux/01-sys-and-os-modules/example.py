"""
Lesson 01 (Module 02): The sys and os Modules
Example Script: Configuration & Certificate Pre-Flight Auditor
"""
import sys
import os

def audit_directory_assets(base_dir):
    print("========================================")
    print("      CONFIG & CERTIFICATE AUDIT        ")
    print("========================================")
    print(f"Auditing Directory: {os.path.abspath(base_dir)}")
    
    if not os.path.exists(base_dir):
        print(f"[!] ERROR: Target directory '{base_dir}' does not exist!")
        return False
        
    required_files = ["app.conf", "tls.crt", "tls.key"]
    missing = []
    
    for filename in required_files:
        full_path = os.path.join(base_dir, filename)
        if os.path.exists(full_path):
            size_kb = round(os.path.getsize(full_path) / 1024, 2)
            print(f"[FOUND]   {filename:<12} ({size_kb} KB)")
        else:
            print(f"[MISSING] {filename:<12} (CRITICAL)")
            missing.append(filename)
            
    print("========================================")
    if missing:
        print(f"[!] FAILED: Missing required deployment assets: {missing}")
        return False
        
    print("[+] All configuration assets verified successfully.")
    return True

if __name__ == "__main__":
    # If no argument passed, audit current directory
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    is_valid = audit_directory_assets(target)
    sys.exit(0 if is_valid else 1)
