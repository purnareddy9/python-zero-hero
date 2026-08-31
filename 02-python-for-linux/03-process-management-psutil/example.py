"""
Lesson 03 (Module 02): Process Management and System Metrics with psutil
Example Script: Top Resource Hog Identifier & Memory Auditor
"""
import psutil

def audit_system_and_top_processes(top_n=3):
    print("========================================")
    print("       HOST RESOURCE HEALTH AUDIT       ")
    print("========================================")
    
    # 1. System Level Metrics
    cpu_pct = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"Total CPU Load : {cpu_pct}%")
    print(f"Memory Usage   : {mem.percent}% ({round(mem.used / (1024**3), 2)} GB / {round(mem.total / (1024**3), 2)} GB)")
    print(f"Root Disk Usage: {disk.percent}% ({round(disk.used / (1024**3), 2)} GB / {round(disk.total / (1024**3), 2)} GB)")
    print("----------------------------------------")
    
    # 2. Querying Active Processes
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
        try:
            info = proc.info
            if info['name']:
                processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    # Sort processes by memory consumption descending
    top_memory = sorted(processes, key=lambda p: p.get('memory_percent') or 0.0, reverse=True)[:top_n]
    
    print(f"Top {top_n} Memory-Consuming Processes:")
    for rank, p in enumerate(top_memory, start=1):
        mem_pct = round(p.get('memory_percent') or 0.0, 2)
        print(f"  {rank}. PID: {p['pid']:<7} | Process: {p['name']:<20} | Mem: {mem_pct:>5}%")
        
    print("========================================")

if __name__ == "__main__":
    audit_system_and_top_processes(top_n=3)
