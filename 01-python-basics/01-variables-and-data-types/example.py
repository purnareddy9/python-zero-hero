"""
Lesson 01: Variables and Data Types
Example Script: Server Inventory Metadata Collector
"""

# 1. Defining Server Attributes
hostname = "k8s-worker-node-04"
ssh_port = 22
memory_used_pct = 74.2
is_draining = False

# 2. Type Inspection
print("========================================")
print("       NODE CONFIGURATION AUDIT         ")
print("========================================")
print(f"Hostname      : {hostname} (Type: {type(hostname).__name__})")
print(f"SSH Port      : {ssh_port} (Type: {type(ssh_port).__name__})")
print(f"Memory Usage  : {memory_used_pct}% (Type: {type(memory_used_pct).__name__})")
print(f"Draining Mode : {is_draining} (Type: {type(is_draining).__name__})")

# 3. Real DevOps Challenge: Converting String to Integer from Environment / Config
port_str = "8080"
# port_num = port_str + 1  # ❌ TypeError!
port_num = int(port_str) + 1  # ✅ Correct type casting
print(f"Next Available Port: {port_num}")
print("========================================")
