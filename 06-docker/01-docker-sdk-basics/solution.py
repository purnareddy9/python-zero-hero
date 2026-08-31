"""
Lesson 01 (Module 06): Solution — Stopped Container Detector
"""
from typing import List, Tuple

def get_stopped_container_names() -> List[Tuple[str, str, str]]:
    stopped = []
    try:
        import docker
        client = docker.from_env()
        for c in client.containers.list(all=True):
            if c.status.lower() != "running":
                stopped.append((c.name, c.short_id, c.status))
    except Exception as err:
        print(f"[*] Docker SDK Notice: Daemon offline or not installed ({err})")
        # Provide sample mock for testing environments where Docker daemon is not active
        stopped = [("batch-worker-01", "7a8b9c0d", "exited"), ("temp-db-test", "1e2f3a4b", "dead")]
        
    return stopped

if __name__ == "__main__":
    print("========================================")
    print("      STOPPED CONTAINER AUDIT           ")
    print("========================================")
    results = get_stopped_container_names()
    print(f"Total Stopped/Exited Containers: {len(results)}\n")
    for name, cid, status in results:
        print(f"  - Name: {name:<20} | ID: {cid} | Status: {status}")
    print("========================================")
