"""
Capstone Module: Kubernetes Operations
"""

def run_k8s_audit(namespace="all"):
    print("=========================================")
    print("       KUBERNETES CLUSTER AUDITOR        ")
    print("=========================================")
    print(f"Target Namespace: {namespace}\n")
    
    try:
        from kubernetes import client, config
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
            
        v1 = client.CoreV1Api()
        if namespace.lower() == "all":
            pods = v1.list_pod_for_all_namespaces(timeout_seconds=5).items
        else:
            pods = v1.list_namespaced_pod(namespace=namespace, timeout_seconds=5).items
            
        print(f"Total Workloads: {len(pods)} pods")
        for p in pods:
            print(f"  - [{p.status.phase.upper():<7}] NS: {p.metadata.namespace:<12} | Pod: {p.metadata.name}")
    except Exception as err:
        print(f"[*] Simulation Mode (K8s API offline: {err})")
        print("  - [RUNNING] NS: production   | Pod: auth-api-99ab-11cc")
        print("  - [RUNNING] NS: production   | Pod: payment-worker-88da-99bf")
        print("  - [PENDING] NS: staging      | Pod: canary-web-33ee-00ff")
        
    print("=========================================")
