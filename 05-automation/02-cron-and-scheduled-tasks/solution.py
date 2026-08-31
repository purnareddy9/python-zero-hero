"""
Lesson 02 (Module 05): Solution — File Lock Guard
"""
import os
import time

def safe_cron_runner(lock_filepath: str) -> bool:
    print("========================================")
    print("      CONCURRENT RUNTIME LOCK GUARD     ")
    print("========================================")
    
    # 1. Acquire Lock
    if os.path.exists(lock_filepath):
        try:
            with open(lock_filepath, "r") as f:
                active_pid = f.read().strip()
        except Exception:
            active_pid = "Unknown"
        print(f"[!] ABORT: Another process (PID: {active_pid}) holds lock '{lock_filepath}'.")
        print("========================================")
        return False
        
    try:
        # Write PID to lock file
        with open(lock_filepath, "w") as f:
            f.write(str(os.getpid()))
        print(f"[+] Lock acquired successfully by PID {os.getpid()}.")
        
        # 2. Execute Task Logic
        print("[*] Running background cleanup operations...")
        time.sleep(1.0)
        print("[+] Background maintenance completed.")
        return True
        
    finally:
        # 3. Guaranteed Lock Release
        if os.path.exists(lock_filepath):
            os.remove(lock_filepath)
            print(f"[+] Lock file '{lock_filepath}' released.")
            print("========================================")

if __name__ == "__main__":
    lock_file = "test_cron.lock"
    safe_cron_runner(lock_file)
