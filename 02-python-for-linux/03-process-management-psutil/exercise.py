"""
Lesson 03 (Module 02): Exercise — Orphan Process Watchdog

Task:
Write a function `find_processes_by_name(search_term: str)`:
1. Iterates through all running processes using `psutil.process_iter(['pid', 'name', 'username'])`.
2. Finds all processes where `search_term` is a substring of the process name (case-insensitive).
3. Safely ignores `psutil.NoSuchProcess` or `psutil.AccessDenied`.
4. Returns a list of matching dictionaries: `[{"pid": 123, "name": "python3", "user": "root"}, ...]`.
5. Print a clean summary.
"""
import psutil

# TODO: Implement process scanner using psutil

if __name__ == "__main__":
    # Test searching for 'python'
    pass
