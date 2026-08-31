"""
Lesson 01 (Module 10): Solution — Fix the Broken Pipeline Script
"""

broken_payload = {
    "cluster_name": "k8s-prod",
    "port": "8080",
    "servers": ["node-01", "node-02"]
}

def audit_cluster_payload(payload):
    print("========================================")
    print("     DEFENSIVE PAYLOAD AUDIT TEST       ")
    print("========================================")
    
    # 1. Fix TypeError: Cast port string to int safely
    raw_port = payload.get("port", 80)
    port_num = int(raw_port)
    next_port = port_num + 1
    
    # 2. Fix KeyError: Safe nested dict lookup
    cpu_usage = payload.get("metrics", {}).get("cpu", "N/A")
    
    # 3. Fix IndexError: Safe list indexing with length check
    servers = payload.get("servers", [])
    primary_server = servers[0] if len(servers) > 0 else "None"
    
    print(f"Cluster Name  : {payload.get('cluster_name', 'Unknown')}")
    print(f"Next Port     : {next_port}")
    print(f"CPU Metric    : {cpu_usage}")
    print(f"Primary Server: {primary_server}")
    print("========================================")
    return True

if __name__ == "__main__":
    audit_cluster_payload(broken_payload)
