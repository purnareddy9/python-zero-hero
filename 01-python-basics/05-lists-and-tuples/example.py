"""
Lesson 05: Lists and Tuples
Example Script: Server Pool Management & Port Auditor
"""

# 1. Defining and mutating a cluster worker pool
active_nodes = ["worker-east-01", "worker-east-02", "worker-east-03"]
print(f"[*] Initial Active Node Pool ({len(active_nodes)}): {active_nodes}")

# New node auto-scaled up
active_nodes.append("worker-east-04")
print(f"[+] Scaled up! Node added. Current pool: {active_nodes}")

# A node failed health checks -> remove from load balancer pool
failed_node = "worker-east-02"
if failed_node in active_nodes:
    active_nodes.remove(failed_node)
    print(f"[!] Health check failed for {failed_node}. Removed from active pool.")

# 2. Immutable Configuration Tuples for Service Binding
# Format: (Service Name, Bind Port, Protocol)
STANDARD_PORTS = (
    ("SSH", 22, "TCP"),
    ("HTTP", 80, "TCP"),
    ("HTTPS", 443, "TCP"),
    ("PROMETHEUS", 9090, "TCP")
)

print("\n========================================")
print("     STANDARD PORT SECURITY POLICY      ")
print("========================================")
for service, port, proto in STANDARD_PORTS:
    print(f"Service: {service:<12} | Port: {port:<5} | Protocol: {proto}")
print("========================================")
