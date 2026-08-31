"""
Lesson 03: Exercise — Cluster Capacity & Pod Sizing Calculator

Task:
You are provisioning a Kubernetes cluster.
Given:
- `node_count`: 4 nodes
- `ram_per_node_gb`: 16.0 GB
- `reserved_system_ram_gb`: 2.0 GB per node (for OS/Kubelet)
- `current_used_ram_gb`: 34.5 GB
- `pod_ram_requirement_gb`: 4.0 GB

Calculate:
1. `effective_total_ram`: Total RAM available for workloads (excluding system reserved).
2. `remaining_ram`: RAM still free for new pods.
3. `cluster_used_pct`: Percentage of effective RAM currently in use.
4. `additional_pods_capacity`: How many complete pods of size `pod_ram_requirement_gb` can fit.
5. Print a clean capacity report.
"""

node_count = 4
ram_per_node_gb = 16.0
reserved_system_ram_gb = 2.0
current_used_ram_gb = 34.5
pod_ram_requirement_gb = 4.0

# TODO: Perform cluster capacity calculations
