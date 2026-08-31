"""
Lesson 03 (Module 06): Automated Docker Housekeeping and Stale Resource Pruner
Example Script: Automated CI/CD Host Storage Pruner & Housekeeper
"""

def run_docker_host_prune():
    print("========================================")
    print("     DOCKER HOST STORAGE HOUSEKEEPER    ")
    print("========================================")
    
    try:
        import docker
        client = docker.from_env()
        client.ping()
        
        cont_result = client.containers.prune()
        deleted_containers = cont_result.get("ContainersDeleted") or []
        
        img_result = client.images.prune(filters={"dangling": True})
        deleted_images = img_result.get("ImagesDeleted") or []
        reclaimed_space = img_result.get("SpaceReclaimed", 0)
        
        vol_result = client.volumes.prune()
        deleted_volumes = vol_result.get("VolumesDeleted") or []
        reclaimed_space += vol_result.get("SpaceReclaimed", 0)
        
        reclaimed_gb = round(reclaimed_space / (1024 ** 3), 2)
        
        print(f"Containers Pruned   : {len(deleted_containers)}")
        print(f"Dangling Images     : {len(deleted_images)}")
        print(f"Orphaned Volumes    : {len(deleted_volumes)}")
        print(f"Total Disk Reclaimed: {reclaimed_gb} GB")
        
    except Exception as err:
        print(f"[*] Notice: Daemon offline or not installed ({err})\n")
        print("[+] Mock Prune Simulation: 4 stopped containers, 12 dangling layers, 3.0 GB reclaimed.")
        
    print("========================================")
    return True

if __name__ == "__main__":
    run_docker_host_prune()
