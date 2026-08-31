"""
Lesson 09: Solution — Dependency Pre-Flight Checker
"""
from typing import List

REQUIRED_DEVOPS_MODULES = ["sys", "os", "json", "math", "platform", "requests", "yaml"]

def check_dependencies(required_modules: List[str]) -> bool:
    print("========================================")
    print("    PIPELINE PRE-FLIGHT MODULE CHECK    ")
    print("========================================")
    
    missing_modules = []
    
    for mod_name in required_modules:
        try:
            __import__(mod_name)
            print(f"[FOUND]   Module '{mod_name}' is available.")
        except (ModuleNotFoundError, ImportError):
            print(f"[MISSING] Module '{mod_name}' is NOT installed.")
            missing_modules.append(mod_name)
            
    print("========================================")
    
    if missing_modules:
        print(f"[!] FAILED: {len(missing_modules)} required module(s) missing.")
        print("\nRemediation Command:")
        print(f"    pip install {' '.join(missing_modules)}")
        print("========================================")
        return False
    else:
        print("[+] All dependencies satisfied. Ready to execute pipeline.")
        print("========================================")
        return True

if __name__ == "__main__":
    check_dependencies(REQUIRED_DEVOPS_MODULES)
