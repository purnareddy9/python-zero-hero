"""
Lesson 03 (Module 06): Solution — Ephemeral Container Cleaner
"""

def purge_ephemeral_containers(prefix="test-runner-", dry_run=True) -> int:
    print("========================================")
    print("      EPHEMERAL CONTAINER CLEANER       ")
    print("========================================")
    print(f"Target Prefix: '{prefix}' | Dry-Run: {dry_run}\n")
    
    count = 0
    try:
        import docker
        client = docker.from_env()
        for c in client.containers.list(all=True):
            if c.name.startswith(prefix):
                count += 1
                if dry_run:
                    print(f"[DRY-RUN] Would purge: {c.name:<25} (ID: {c.short_id})")
                else:
                    c.remove(force=True)
                    print(f"[PURGED]  Removed: {c.name:<25} (ID: {c.short_id})")
    except Exception as err:
        print(f"[*] Simulation Mode (Docker engine offline: {err})")
        mock_containers = [f"{prefix}01", f"{prefix}02", f"{prefix}03"]
        for name in mock_containers:
            count += 1
            print(f"[SIMULATION] Identified ephemeral target: {name}")
            
    print("----------------------------------------")
    print(f"Total Ephemeral Containers Identified: {count}")
    print("========================================")
    return count

if __name__ == "__main__":
    purge_ephemeral_containers(prefix="test-runner-", dry_run=True)
