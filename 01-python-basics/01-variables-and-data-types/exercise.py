"""
Lesson 01: Exercise — Environment Config Validator

Task:
You are building an automated deployer. The values below were read from an environment file
as strings.
1. Convert `raw_node_count` to an integer.
2. Convert `raw_cpu_limit` to a float.
3. Convert `raw_debug_mode` to a boolean (True if value is "true", otherwise False).
4. Check if the cluster is HA ready (requires at least 3 nodes). Set `is_ha_ready` to True/False.
5. Print a clean summary.
"""

raw_cluster_name = "k8s-prod-us-central"
raw_node_count = "5"
raw_cpu_limit = "3.75"
raw_debug_mode = "false"

# TODO: Perform type conversions and validation below
