"""
Lesson 04 (Module 03): Solution — Docker Compose Hardener
"""
import yaml

compose_yaml = """
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
  worker:
    image: python-worker:latest
"""

def harden_compose_spec(yaml_str: str) -> str:
    doc = yaml.safe_load(yaml_str)
    services = doc.get("services", {})
    
    for svc_name, svc_config in services.items():
        # 1. Enforce restart policy
        svc_config["restart"] = "always"
        
        # 2. Eliminate risky :latest tags
        image = svc_config.get("image", "")
        if image.endswith(":latest"):
            svc_config["image"] = image.replace(":latest", ":stable")
            
    # Serialize back to clean YAML
    return yaml.dump(doc, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    print("========================================")
    print("     DOCKER COMPOSE HARDENING AUDIT     ")
    print("========================================")
    hardened = harden_compose_spec(compose_yaml)
    print("Hardened Configuration:")
    print(hardened)
    print("========================================")
