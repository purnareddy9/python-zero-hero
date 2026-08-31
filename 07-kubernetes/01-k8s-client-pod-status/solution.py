"""
Lesson 01 (Module 07): Solution — Namespace Pod Distribution Auditor
"""
from typing import Dict

def get_namespace_pod_distribution() -> Dict[str, int]:
    distribution = {}
    try:
        from kubernetes import client, config
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
            
        v1 = client.CoreV1Api()
        pod_list = v1.list_pod_for_all_namespaces(timeout_seconds=5)
        for pod in pod_list.items:
            ns = pod.metadata.namespace
            distribution[ns] = distribution.get(ns, 0) + 1
    except Exception as err:
        print(f"[*] Simulation Mode (Cluster API offline: {err})")
        distribution = {
            "kube-system": 12,
            "ingress-nginx": 3,
            "production": 18,
            "staging": 6,
            "monitoring": 8
        }
        
    return distribution

if __name__ == "__main__":
    print("========================================")
    print("     K8S NAMESPACE POD DISTRIBUTION     ")
    print("========================================")
    dist = get_namespace_pod_distribution()
    total_pods = sum(dist.values())
    print(f"Total Cluster Workloads: {total_pods} pods\n")
    for ns, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
        pct = round((count / total_pods) * 100, 1)
        print(f"  - {ns:<18} : {count:>3} pods ({pct:>4}%)")
    print("========================================")
