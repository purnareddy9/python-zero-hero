"""
Lesson 07: Solution — Fleet Disk Space Auditor
"""

fleet_disks = {
    "web-01": 45,
    "web-02": 82,
    "web-03": 30,
    "web-04": 94,
    "web-05": 78
}

print("========================================")
print("       FLEET DISK THRESHOLD AUDIT       ")
print("========================================")

for server, usage in fleet_disks.items():
    # 1. Skip healthy, low-usage servers to minimize log noise
    if usage < 50:
        continue
        
    # 2. Halt immediately on critical threshold breach
    if usage >= 90:
        print(f"[!] [CRITICAL EMERGENCY] Host {server} is at {usage}% disk! Halting audit.")
        break
        
    # 3. Log warning servers
    print(f"[*] [WARNING] Host {server} is elevated at {usage}% disk.")

print("========================================")
