"""
Lesson 01 (Module 07): The Official Kubernetes Python Client: Pods and Nodes
Example Script: Kubernetes Namespace & Pod Fleet Health Inspector
"""

def audit_kubernetes_cluster_pods():
    print("========================================")
    print("     KUBERNETES POD FLEET AUDITOR       ")
    print("========================================")
    
    try:
        from kubernetes import client, config
        try:
            config.load_incluster_config()
            print("[*] Loaded In-Cluster ServiceAccount authentication.")
        except Exception:
            config.load_kube_config()
            print("[*] Loaded local ~/.kube/config authentication.")
            
        v1 = client.CoreV1Api()
        pod_list = v1.list_pod_for_all_namespaces(timeout_seconds=5)
        
        print(f"\nTotal Cluster Pods: {len(pod_list.items)}\n")
        
        for pod in pod_list.items:
            ns = pod.metadata.namespace
            name = pod.metadata.name
            phase = pod.status.phase
            pod_ip = pod.status.pod_ip or "No IP"
            
            tag = "[RUNNING]" if phase == "Running" else f"[{phase.upper()}]"
            print(f"{tag:<10} NS: {ns:<12} | Pod: {name:<30} | IP: {pod_ip}")
            
    except Exception as err:
        print(f"[*] Simulating K8s API response (Cluster offline: {err})\n")
        mock_pods = [
            ("production", "payment-api-78bf-x9da", "Running", "10.244.1.15"),
            ("production", "order-worker-55cc-11aa", "Running", "10.244.2.24"),
            ("staging", "auth-canary-99ea-44bb", "Pending", "No IP")
        ]
        for ns, name, phase, ip in mock_pods:
            tag = f"[{phase.upper()}]"
            print(f"{tag:<10} NS: {ns:<12} | Pod: {name:<30} | IP: {ip}")
            
    print("========================================")

if __name__ == "__main__":
    audit_kubernetes_cluster_pods()
