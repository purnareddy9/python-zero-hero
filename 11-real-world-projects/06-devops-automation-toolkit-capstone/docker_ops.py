"""
Capstone Module: Docker Operations
"""

def run_docker_audit(do_prune=False):
    print("=========================================")
    print("         DOCKER FLEET OPERATIONS        ")
    print("=========================================")
    
    try:
        import docker
        client = docker.from_env()
        containers = client.containers.list(all=True)
        print(f"Active/Stopped Containers: {len(containers)}")
        for c in containers:
            print(f"  - [{c.status.upper():<7}] {c.name:<20} ({c.image.tags[0] if c.image.tags else c.image.short_id})")
        if do_prune:
            print("\n[*] Pruning stopped containers...")
            client.containers.prune()
            print("[+] Prune completed.")
    except Exception as err:
        print(f"[*] Simulation Mode (Docker engine offline: {err})")
        print("  - [RUNNING] payment-redis-prod   (redis:7-alpine)")
        print("  - [STOPPED] temp-test-worker     (python:3.11-slim)")
        if do_prune:
            print("[+] [SIMULATED] Pruned 1 stopped container.")
            
    print("=========================================")
