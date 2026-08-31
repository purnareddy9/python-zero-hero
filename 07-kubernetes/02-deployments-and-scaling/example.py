"""
Lesson 02 (Module 07): Deployments, Replica Scaling, and Image Rolling Updates
Example Script: Kubernetes Autoscaling & Rollout Status Inspector
"""

def audit_and_scale_deployment(deployment_name="payment-api", namespace="production", target_replicas=4):
    print("========================================")
    print("     K8S DEPLOYMENT CONTROLLER AUDIT    ")
    print("========================================")
    print(f"Target: {namespace}/{deployment_name}\n")
    
    try:
        from kubernetes import client, config
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
            
        apps_v1 = client.AppsV1Api()
        
        deployment = apps_v1.read_namespaced_deployment(name=deployment_name, namespace=namespace)
        current_replicas = deployment.spec.replicas
        available_replicas = deployment.status.available_replicas or 0
        container_image = deployment.spec.template.spec.containers[0].image
        
        print(f"Active Image       : {container_image}")
        print(f"Configured Replicas: {current_replicas}")
        print(f"Available Replicas : {available_replicas}")
        
        if current_replicas != target_replicas:
            print(f"[*] Scaling deployment from {current_replicas} -> {target_replicas} replicas...")
            scale_body = {"spec": {"replicas": target_replicas}}
            apps_v1.patch_namespaced_deployment_scale(
                name=deployment_name,
                namespace=namespace,
                body=scale_body
            )
            print("[+] Scale patch applied successfully.")
        else:
            print("[*] Replicas already at target count. No scale action needed.")
            
    except Exception as err:
        print(f"[*] Simulating Deployment scaling (Cluster offline: {err})\n")
        print(f"Active Image       : myregistry.io/payment:v1.4.0")
        print(f"Configured Replicas: 2")
        print(f"Available Replicas : 2")
        print(f"[+] [SIMULATED] Scale patch: Scaled {deployment_name} to {target_replicas} replicas.")
        
    print("========================================")

if __name__ == "__main__":
    audit_and_scale_deployment("payment-api", "production", target_replicas=4)
