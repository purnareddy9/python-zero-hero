"""
Lesson 01 (Module 03): Safe File I/O and Configuration Backups
Example Script: Safe Config File Modifier with Timestamped Backup
"""
import os
import shutil
import time

def update_config_setting(config_path, target_key, new_value):
    print("========================================")
    print("      CONFIG BACKUP & UPDATE UTILITY    ")
    print("========================================")
    
    if not os.path.exists(config_path):
        print(f"[!] ERROR: Target config '{config_path}' not found.")
        return False
        
    # 1. Create a timestamped backup before touching anything
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = f"{config_path}.bak.{timestamp}"
    shutil.copyfile(config_path, backup_path)
    print(f"[+] Backup created: {backup_path}")
    
    # 2. Read existing configuration lines
    with open(config_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    updated_lines = []
    found = False
    
    for line in lines:
        if line.strip().startswith(f"{target_key}="):
            updated_lines.append(f"{target_key}={new_value}\n")
            found = True
            print(f"[*] Updated: {line.strip()} -> {target_key}={new_value}")
        else:
            updated_lines.append(line)
            
    if not found:
        updated_lines.append(f"{target_key}={new_value}\n")
        print(f"[+] Appended new setting: {target_key}={new_value}")
        
    # 3. Write back changes atomically
    with open(config_path, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
        
    print("[+] Configuration update completed safely.")
    print("========================================")
    return True

if __name__ == "__main__":
    demo_file = "demo_app.conf"
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("# App Configuration\nPORT=8080\nWORKERS=2\nDEBUG=False\n")
        
    update_config_setting(demo_file, "WORKERS", "4")
