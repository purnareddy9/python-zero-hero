"""
Lesson 01 (Module 10): Exercise — Fix the Broken Pipeline Script

Task:
The following function has 3 common beginner bugs:
1. It crashes with `KeyError` if `"metrics"` is missing.
2. It crashes with `TypeError` when calculating `port + 1` on string ports.
3. It crashes with `IndexError` when accessing `servers[3]` on a 2-element list.

Refactor `audit_cluster_payload(payload)` to fix all three bugs defensively!
"""

broken_payload = {
    "cluster_name": "k8s-prod",
    "port": "8080",
    "servers": ["node-01", "node-02"]
    # "metrics" key is missing
}

def audit_cluster_payload(payload):
    # TODO: Fix bugs below
    # port_next = payload["port"] + 1
    # cpu = payload["metrics"]["cpu"]
    # primary = payload["servers"][3]
    pass

if __name__ == "__main__":
    pass
