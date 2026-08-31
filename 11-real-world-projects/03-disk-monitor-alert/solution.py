"""
Project 03: Solution — Automated Disk Remediation Purger
"""
import os

def auto_remediate_disk(target_dir: str, usage_pct: float, threshold: float = 90.0) -> bool:
    print("=========================================")
    print("     AUTOMATED DISK REMEDIATION ENGINE   ")
    print("=========================================")
    print(f"Directory Target: {target_dir}")
    print(f"Current Usage   : {usage_pct}% (Threshold: {threshold}%)\n")
    
    if usage_pct < threshold:
        print("[NORMAL] Disk capacity is healthy. No cleanup action needed.")
        print("=========================================")
        return False
        
    print("[!] THRESHOLD BREACHED: Triggering emergency archive purge...")
    purged_bytes = 0
    purged_files = 0
    
    if os.path.exists(target_dir):
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(".gz") or file.endswith(".old") or file.endswith(".tmp"):
                    full_path = os.path.join(root, file)
                    try:
                        size = os.path.getsize(full_path)
                        os.remove(full_path)
                        purged_bytes += size
                        purged_files += 1
                        print(f"  [PURGED] {file} ({size} bytes)")
                    except Exception as err:
                        print(f"  [FAIL] Unable to remove {file}: {err}")
                        
    reclaimed_mb = round(purged_bytes / (1024 ** 2), 2)
    print("-----------------------------------------")
    print(f"Remediation Summary: {purged_files} files deleted, {reclaimed_mb} MB reclaimed.")
    print("=========================================")
    return True

if __name__ == "__main__":
    demo_dir = "./emergency_logs"
    os.makedirs(demo_dir, exist_ok=True)
    with open(os.path.join(demo_dir, "syslog.1.gz"), "w") as f:
        f.write("A" * 5000)
    with open(os.path.join(demo_dir, "temp_data.old"), "w") as f:
        f.write("B" * 10000)
        
    auto_remediate_disk(demo_dir, usage_pct=94.5, threshold=90.0)
