"""
Lesson 03: Numbers and Math
Example Script: Host Disk Capacity Calculator & Cloud Cost Estimator
"""

def audit_disk_and_cost(total_bytes, used_bytes, hourly_instance_cost):
    # 1. Byte conversions using exponents
    bytes_in_gb = 1024 ** 3
    total_gb = total_bytes / bytes_in_gb
    used_gb = used_bytes / bytes_in_gb
    free_gb = total_gb - used_gb
    
    # 2. Percentage calculation with rounding
    used_pct = round((used_gb / total_gb) * 100, 1)
    
    # 3. Cloud monthly cost projection (average month = 730 hours)
    monthly_cost = round(hourly_instance_cost * 730, 2)
    
    print("========================================")
    print("     SYSTEM DISK & COST AUDIT REPORT    ")
    print("========================================")
    print(f"Total Storage : {total_gb:.2f} GB")
    print(f"Used Storage  : {used_gb:.2f} GB ({used_pct}%)")
    print(f"Free Storage  : {free_gb:.2f} GB")
    print(f"Hourly Cost   : ${hourly_instance_cost:.4f}/hr")
    print(f"Monthly Est.  : ${monthly_cost:.2f}/month")
    
    if used_pct >= 85.0:
        print("[!] STATUS: CRITICAL - Disk cleanup required")
    elif used_pct >= 70.0:
        print("[!] STATUS: WARNING - Approaching threshold")
    else:
        print("[+] STATUS: HEALTHY")
    print("========================================")

if __name__ == "__main__":
    audit_disk_and_cost(
        total_bytes=536870912000,
        used_bytes=461708984320,
        hourly_instance_cost=0.096
    )
