"""
Lesson 03: Solution — Cluster Capacity & Pod Sizing Calculator
"""

node_count = 4
ram_per_node_gb = 16.0
reserved_system_ram_gb = 2.0
current_used_ram_gb = 34.5
pod_ram_requirement_gb = 4.0

# 1. Effective Capacity Calculations
effective_ram_per_node = ram_per_node_gb - reserved_system_ram_gb
effective_total_ram = node_count * effective_ram_per_node
remaining_ram = effective_total_ram - current_used_ram_gb

# 2. Percentage and Pod Sizing
cluster_used_pct = round((current_used_ram_gb / effective_total_ram) * 100, 1)
# Floor division ensures we only count complete pods
additional_pods_capacity = int(remaining_ram // pod_ram_requirement_gb)

# 3. Print Report
print("========================================")
print("     KUBERNETES CLUSTER CAPACITY        ")
print("========================================")
print(f"Total Nodes          : {node_count}")
print(f"Effective Workload RAM: {effective_total_ram:.1f} GB")
print(f"Current Memory Used  : {current_used_ram_gb:.1f} GB ({cluster_used_pct}%)")
print(f"Available Workload RAM: {remaining_ram:.1f} GB")
print(f"Pod Size Requirement : {pod_ram_requirement_gb:.1f} GB")
print(f"Max Extra Pods Fit   : {additional_pods_capacity} pods")
print("========================================")
