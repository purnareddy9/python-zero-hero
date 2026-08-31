"""
Lesson 03 (Module 07): Detecting CrashLoopBackOff and Pod Failures
Example Script: Kubernetes CrashLoopBackOff & OOMKilled Incident Detector
"""

def scan_for_crashlooping_pods():
    print("========================================")
    print("     K8S CRASHLOOP & OOM DETECTOR       ")
    print("========================================")
    
    try:
        from kubernetes import client, config
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
            
        v1 = client.CoreV1Api()
        pods = v1.list_pod_for_all_namespaces(timeout_seconds=5)
        
        incidents = []
        for pod in pods.items:
            ns = pod.metadata.namespace
            name = pod.metadata.name
            
            if not pod.status.container_statuses:
                continue
                
            for cs in pod.status.container_statuses:
                restarts = cs.restart_count
                waiting = cs.state.waiting
                
                if waiting and waiting.reason in ["CrashLoopBackOff", "ImagePullBackOff", "CreateContainerConfigError"]:
                    last_exit = "N/A"
                    if cs.last_state and cs.last_state.terminated:
                        last_exit = cs.last_state.terminated.exit_code
                        
                    incidents.append({
                        "namespace": ns,
                        "pod": name,
                        "container": cs.name,
                        "reason": waiting.reason,
                        "restarts": restarts,
                        "last_exit_code": last_exit
                    })
                    
        print(f"Total Failing Pods Identified: {len(incidents)}\n")
        for inc in incidents:
            print(f"[!] INCIDENT DETECTED:")
            print(f"    Namespace    : {inc['namespace']}")
            print(f"    Pod Name     : {inc['pod']}")
            print(f"    Container    : {inc['container']}")
            print(f"    Failure State: {inc['reason']}")
            print(f"    Restart Count: {inc['restarts']}")
            print(f"    Last ExitCode: {inc['last_exit_code']}\n")
            
    except Exception as err:
        print(f"[*] Simulating crash detection (Cluster offline: {err})\n")
        print("[!] [SIMULATED INCIDENT]:")
        print("    Namespace    : production")
        print("    Pod Name     : payment-worker-88da-99bf")
        print("    Container    : worker")
        print("    Failure State: CrashLoopBackOff")
        print("    Restart Count: 14")
        print("    Last ExitCode: 137 (OOMKilled - Out Of Memory)")
        
    print("========================================")

if __name__ == "__main__":
    scan_for_crashlooping_pods()
