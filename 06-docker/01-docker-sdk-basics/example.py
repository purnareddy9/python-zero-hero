"""
Lesson 01 (Module 06): Docker SDK for Python
Example Script: Docker Container Fleet Health Auditor
"""
import sys

def audit_docker_containers():
    print("========================================")
    print("      DOCKER CONTAINER FLEET AUDIT      ")
    print("========================================")
    
    try:
        import docker
        client = docker.from_env()
        client.ping()
    except ImportError:
        print("[!] Missing 'docker' package. Install via: pip install docker")
        return False
    except Exception as err:
        print(f"[!] DOCKER DAEMON OFFLINE / UNREACHABLE: {err}")
        print("    Ensure Docker Desktop / dockerd service is running.")
        return False
        
    containers = client.containers.list(all=True)
    print(f"Total Containers Found: {len(containers)}\n")
    
    if not containers:
        print("[*] No active or stopped containers found.")
        print("========================================")
        return True
        
    for c in containers:
        status = c.status.upper()
        tag = "[RUNNING]" if status == "RUNNING" else "[STOPPED]"
        image_tag = c.image.tags[0] if c.image.tags else c.image.short_id
        print(f"{tag:<10} ID: {c.short_id} | Name: {c.name:<20} | Image: {image_tag}")
        
    print("========================================")
    return True

if __name__ == "__main__":
    audit_docker_containers()
