"""
Lesson 06: Dictionaries and Sets
Example Script: Kubernetes Node Metadata Aggregator & Firewall Drift Auditor
"""

# 1. Nested Dictionaries (simulating K8s API JSON response)
cluster_nodes = {
    "node-east-01": {
        "status": "Ready",
        "cpu_cores": 8,
        "labels": {"zone": "us-east-1a", "tier": "frontend"}
    },
    "node-east-02": {
        "status": "NotReady",
        "cpu_cores": 8,
        "labels": {"zone": "us-east-1b", "tier": "backend"}
    }
}

print("========================================")
print("       CLUSTER NODE HEALTH AUDIT        ")
print("========================================")
for node_name, details in cluster_nodes.items():
    status = details.get("status", "Unknown")
    zone = details.get("labels", {}).get("zone", "unassigned")
    print(f"Node: {node_name:<14} | Status: {status:<8} | Zone: {zone}")

# 2. Sets for Configuration Drift Detection
desired_firewall_ports = {22, 80, 443, 8080}
actual_open_ports = {22, 80, 443, 8080, 3306, 9200}  # 3306 and 9200 should not be open publicly!

# Find unexpected open ports (Security Drift)
unauthorized_ports = actual_open_ports - desired_firewall_ports

# Find missing required ports
missing_ports = desired_firewall_ports - actual_open_ports

print("\n========================================")
print("     FIREWALL SECURITY DRIFT AUDIT      ")
print("========================================")
print(f"Desired Ports : {desired_firewall_ports}")
print(f"Active Ports  : {actual_open_ports}")
if unauthorized_ports:
    print(f"[!] SECURITY ALERT: Unauthorized ports open: {unauthorized_ports}")
if missing_ports:
    print(f"[!] WARNING: Required ports missing: {missing_ports}")
if not unauthorized_ports and not missing_ports:
    print("[+] Firewall rules match desired state.")
print("========================================")
