"""
Lesson 02 (Module 05): Scheduled Automation, Cron, and Background Jobs
Example Script: Automated Log Retention Cleaner with Overlap Lock Protection
"""
import os
import time

def purge_old_log_files(target_dir, retention_days=14, dry_run=False):
    print("========================================")
    print("       LOG RETENTION & PURGE AUDIT      ")
    print("========================================")
    print(f"Target Directory: {os.path.abspath(target_dir)}")
    print(f"Retention Period: {retention_days} days (Dry-Run: {dry_run})\n")
    
    if not os.path.exists(target_dir):
        print(f"[!] Directory '{target_dir}' does not exist.")
        return 0
        
    cutoff_timestamp = time.time() - (retention_days * 86400)
    purged_count = 0
    reclaimed_bytes = 0
    
    for filename in os.listdir(target_dir):
        if not filename.endswith(".log"):
            continue
            
        full_path = os.path.join(target_dir, filename)
        if not os.path.isfile(full_path):
            continue
            
        mtime = os.path.getmtime(full_path)
        file_size = os.path.getsize(full_path)
        age_days = round((time.time() - mtime) / 86400, 1)
        
        if mtime < cutoff_timestamp:
            purged_count += 1
            reclaimed_bytes += file_size
            if dry_run:
                print(f"[DRY-RUN] Would delete: {filename:<25} (Age: {age_days} days, Size: {file_size} bytes)")
            else:
                os.remove(full_path)
                print(f"[DELETED] Purged: {filename:<25} (Age: {age_days} days, Reclaimed: {file_size} bytes)")
        else:
            print(f"[KEPT]    Retained: {filename:<23} (Age: {age_days} days)")
            
    print("----------------------------------------")
    reclaimed_mb = round(reclaimed_bytes / (1024 ** 2), 2)
    print(f"Purge Summary : {purged_count} files removed.")
    print(f"Space Reclaimed: {reclaimed_mb} MB")
    print("========================================")
    return purged_count

if __name__ == "__main__":
    demo_dir = "./mock_log_dir"
    os.makedirs(demo_dir, exist_ok=True)
    
    old_log = os.path.join(demo_dir, "app_old.log")
    recent_log = os.path.join(demo_dir, "app_recent.log")
    
    with open(old_log, "w") as f:
        f.write("Old log entry data\n" * 100)
    with open(recent_log, "w") as f:
        f.write("Recent log entry data\n" * 100)
        
    twenty_days_ago = time.time() - (20 * 86400)
    os.utime(old_log, (twenty_days_ago, twenty_days_ago))
    
    purge_old_log_files(demo_dir, retention_days=14, dry_run=False)
