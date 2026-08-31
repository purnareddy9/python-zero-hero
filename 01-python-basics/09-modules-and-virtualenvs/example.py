"""
Lesson 09: Modules, Imports, Pip, and Virtual Environments
Example Script: Module Inspection & Runtime Environment Audit
"""
import sys
import os
import platform

def audit_python_runtime():
    print("========================================")
    print("     PYTHON RUNTIME ENVIRONMENT AUDIT   ")
    print("========================================")
    
    # 1. Inspecting Python Binary & Version
    python_bin = sys.executable
    version = sys.version.split(" ")[0]
    
    # 2. Detecting if running inside a Virtual Environment
    is_in_venv = hasattr(sys, 'real_prefix') or (sys.prefix != getattr(sys, 'base_prefix', sys.prefix))
    
    print(f"Host Node      : {platform.node()}")
    print(f"OS Platform    : {platform.system()} {platform.release()}")
    print(f"Python Executable: {python_bin}")
    print(f"Python Version : {version}")
    print(f"In VirtualEnv  : {is_in_venv}")
    
    if not is_in_venv:
        print("\n[!] WARNING: Running against global/system Python!")
        print("    Recommendation: Create an isolated venv to avoid package contamination.")
    else:
        print("\n[+] SUCCESS: Running inside isolated virtual environment.")
        
    print("========================================")

if __name__ == "__main__":
    audit_python_runtime()
