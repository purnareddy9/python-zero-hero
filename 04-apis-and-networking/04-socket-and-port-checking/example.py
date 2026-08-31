"""
Lesson 04 (Module 04): Sockets, TCP Port Probing, and Network Reachability
Example Script: High-Speed Multi-Host TCP Port Scanner & Reachability Auditor
"""
import socket

def audit_infrastructure_ports(target_host, ports_to_scan):
    print("========================================")
    print("      TCP PORT REACHABILITY AUDIT       ")
    print("========================================")
    print(f"Target Host: {target_host}")
    
    try:
        ip_addr = socket.gethostbyname(target_host)
        print(f"Resolved IP: {ip_addr}\n")
    except socket.gaierror:
        print(f"[!] DNS RESOLUTION ERROR: Unable to resolve '{target_host}'")
        return False
        
    results = {}
    
    for port, label in ports_to_scan.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.5)
            status_code = sock.connect_ex((ip_addr, port))
            
            is_open = status_code == 0
            results[port] = is_open
            
            tag = "[OPEN]  " if is_open else "[CLOSED]"
            print(f"{tag} Port {port:<5} ({label})")
            
    print("========================================")
    open_count = sum(1 for status in results.values() if status)
    print(f"Audit Summary: {open_count}/{len(ports_to_scan)} ports listening.")
    print("========================================")
    return results

if __name__ == "__main__":
    standard_devops_ports = {
        80: "HTTP",
        443: "HTTPS",
        22: "SSH",
        3306: "MySQL",
        5432: "PostgreSQL",
        8080: "App Server"
    }
    
    audit_infrastructure_ports("1.1.1.1", standard_devops_ports)
