"""
Lesson 03 (Module 02): Solution — Orphan Process Watchdog
"""
import psutil
from typing import List, Dict, Any

def find_processes_by_name(search_term: str) -> List[Dict[str, Any]]:
    matches = []
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            name = info.get('name') or ""
            if search_term.lower() in name.lower():
                matches.append({
                    "pid": info['pid'],
                    "name": name,
                    "user": info.get('username') or "N/A"
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    return matches

if __name__ == "__main__":
    search = "python"
    print("========================================")
    print(f"      PROCESS SCANNER: '{search}'       ")
    print("========================================")
    
    found = find_processes_by_name(search)
    print(f"Total Matches Found: {len(found)}\n")
    
    for item in found:
        print(f"  PID: {item['pid']:<7} | User: {item['user']:<15} | Process: {item['name']}")
        
    print("========================================")
