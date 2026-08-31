"""
Lesson 00: Solution — Service Health Validator
"""
import sys

services = {
    "auth-service": 200,
    "payment-gateway": 503,
    "user-profile": 200,
    "order-processor": 500
}

def audit_services(service_map):
    print("========================================")
    print("       MICROSERVICE HEALTH AUDIT        ")
    print("========================================")
    
    failed_services = []
    
    for service_name, status_code in service_map.items():
        if status_code == 200:
            print(f"[OK]      {service_name:<20} -> Status: {status_code}")
        else:
            print(f"[FAILED]  {service_name:<20} -> Status: {status_code}")
            failed_services.append((service_name, status_code))
            
    print("========================================")
    
    if failed_services:
        print(f"\n[!] CRITICAL: {len(failed_services)} service(s) are failing!")
        for svc, code in failed_services:
            print(f"    - {svc} returned HTTP {code}")
        print("\nExiting with status code 1 (Failure)")
        sys.exit(1)
    else:
        print("\n[+] All systems operational.")
        print("Exiting with status code 0 (Success)")
        sys.exit(0)

if __name__ == "__main__":
    audit_services(services)
