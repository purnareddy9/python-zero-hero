"""
Lesson 02 (Module 02): The subprocess Module
Example Script: Linux System Service & Command Orchestrator
"""
import subprocess
import sys

def execute_command(cmd_list, timeout_sec=5):
    """
    Executes a system command safely and returns (success_bool, stdout_str, stderr_str).
    """
    cmd_display = " ".join(cmd_list)
    print(f"[*] Executing: '{cmd_display}' (Timeout: {timeout_sec}s)")
    
    try:
        proc = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False
        )
        
        if proc.returncode == 0:
            return True, proc.stdout.strip(), ""
        else:
            return False, proc.stdout.strip(), proc.stderr.strip()
            
    except subprocess.TimeoutExpired:
        return False, "", f"Command timed out after {timeout_sec} seconds."
    except FileNotFoundError:
        return False, "", f"Executable '{cmd_list[0]}' was not found on host PATH."

if __name__ == "__main__":
    print("========================================")
    print("     SUBPROCESS COMMAND EXECUTION       ")
    print("========================================")
    
    # 1. Test standard command (Python version)
    ok, out, err = execute_command([sys.executable, "--version"])
    if ok:
        print(f"[SUCCESS] Python Runtime: {out}")
    else:
        print(f"[FAILED]  Error: {err}")
        
    # 2. Test disk check command (platform-aware)
    disk_cmd = ["df", "-h"] if sys.platform != "win32" else ["cmd", "/c", "dir"]
    ok, out, err = execute_command(disk_cmd)
    if ok:
        first_line = out.split("\n")[0]
        print(f"[SUCCESS] Command Output: {first_line}")
    else:
        print(f"[FAILED]  Disk check failed: {err}")
        
    # 3. Test non-existent command handling
    ok, out, err = execute_command(["non_existent_devops_tool"])
    print(f"[DEFENSE] Non-existent tool handled safely: {err}")
    print("========================================")
