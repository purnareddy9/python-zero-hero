"""
Lesson 01 (Module 06): Exercise — Stopped Container Detector

Task:
Write a function `get_stopped_container_names()` using `docker-py`:
1. Attempts to connect to Docker daemon using `docker.from_env()`.
2. Lists all containers (`all=True`).
3. Filters for containers where `c.status != "running"`.
4. Returns a list of tuples: `[(name, short_id, status), ...]`.
5. Handles `ImportError` or connection exceptions gracefully by returning an empty list.
"""

# TODO: Implement get_stopped_container_names function

if __name__ == "__main__":
    pass
