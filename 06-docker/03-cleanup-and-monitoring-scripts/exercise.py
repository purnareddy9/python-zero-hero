"""
Lesson 03 (Module 06): Exercise — Ephemeral Container Cleaner

Task:
Write a function `purge_ephemeral_containers(prefix="test-runner-", dry_run=True)`:
1. Connects to Docker via `docker.from_env()`.
2. Lists all containers (`all=True`).
3. Identifies containers starting with `prefix`.
4. If `dry_run == True`, print `[DRY-RUN] Would remove container: <name>`.
5. If `dry_run == False`, remove container with `c.remove(force=True)` and print `[DELETED] Removed: <name>`.
6. Return the total count of matched containers.
"""

# TODO: Implement purge_ephemeral_containers function

if __name__ == "__main__":
    pass
