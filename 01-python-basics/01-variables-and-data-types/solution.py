"""
Lesson 01: Solution — Environment Config Validator
"""

raw_cluster_name = "k8s-prod-us-central"
raw_node_count = "5"
raw_cpu_limit = "3.75"
raw_debug_mode = "false"

# 1. Type Conversions
cluster_name = str(raw_cluster_name)
node_count = int(raw_node_count)
cpu_limit = float(raw_cpu_limit)
debug_mode = raw_debug_mode.lower() == "true"

# 2. HA Validation Check
is_ha_ready = node_count >= 3

# 3. Formatted Audit Output
print("========================================")
print("     CLUSTER SPECIFICATION AUDIT        ")
print("========================================")
print(f"Cluster Name   : {cluster_name}")
print(f"Node Count     : {node_count} (Type: {type(node_count).__name__})")
print(f"CPU Limit/Node : {cpu_limit} Cores (Type: {type(cpu_limit).__name__})")
print(f"Debug Logging  : {debug_mode} (Type: {type(debug_mode).__name__})")
print(f"HA Ready (>=3) : {is_ha_ready}")
print("========================================")
