"""
Lesson 04 (Module 03): YAML and Configuration Management
Example Script: GitOps CI/CD Image Tag Patcher for Kubernetes Manifests
"""
import yaml

sample_k8s_manifest = """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: auth-service
  namespace: production
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: auth-container
          image: myregistry.io/auth:v1.0.0
          ports:
            - containerPort: 8080
"""

def patch_manifest_image(manifest_yaml_str, new_image_tag):
    print("========================================")
    print("      KUBERNETES MANIFEST PATCHER       ")
    print("========================================")
    
    doc = yaml.safe_load(manifest_yaml_str)
    
    deployment_name = doc["metadata"]["name"]
    container = doc["spec"]["template"]["spec"]["containers"][0]
    old_image = container["image"]
    
    print(f"Deployment Target : {deployment_name}")
    print(f"Current Image     : {old_image}")
    
    container["image"] = new_image_tag
    print(f"Patched Image     : {new_image_tag}\n")
    
    updated_yaml = yaml.dump(doc, default_flow_style=False, sort_keys=False)
    
    print("Generated GitOps Manifest:")
    print("----------------------------------------")
    print(updated_yaml)
    print("========================================")
    return updated_yaml

if __name__ == "__main__":
    new_tag = "myregistry.io/auth:v1.1.0-sha.8f2a1b"
    patch_manifest_image(sample_k8s_manifest, new_tag)
