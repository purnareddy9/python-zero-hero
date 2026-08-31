"""
Lesson 02 (Module 02): Exercise — Git Branch & Commit Auditor

Task:
Write a function `get_git_metadata()` that uses `subprocess.run()`:
1. Run `git rev-parse --abbrev-ref HEAD` to get the current branch name.
2. Run `git rev-parse --short HEAD` to get the current short commit SHA.
3. Catch `FileNotFoundError` (if git is not installed) or failure exit codes (if not in a git repository).
4. Return a dictionary:
   `{"branch": branch_name or "UNKNOWN", "commit": commit_sha or "UNKNOWN", "is_git_repo": True/False}`
5. Print a clean summary.
"""
import subprocess

# TODO: Implement get_git_metadata using subprocess.run

if __name__ == "__main__":
    pass
