"""
Lesson 02 (Module 02): Solution — Git Branch & Commit Auditor
"""
import subprocess
from typing import Dict, Any

def get_git_metadata() -> Dict[str, Any]:
    metadata = {
        "branch": "UNKNOWN",
        "commit": "UNKNOWN",
        "is_git_repo": False
    }
    
    try:
        # 1. Fetch current branch
        branch_proc = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=3,
            check=False
        )
        
        # 2. Fetch short commit hash
        commit_proc = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            timeout=3,
            check=False
        )
        
        if branch_proc.returncode == 0 and commit_proc.returncode == 0:
            metadata["branch"] = branch_proc.stdout.strip()
            metadata["commit"] = commit_proc.stdout.strip()
            metadata["is_git_repo"] = True
            
    except (FileNotFoundError, subprocess.TimeoutExpired):
        metadata["is_git_repo"] = False
        
    return metadata

if __name__ == "__main__":
    print("========================================")
    print("       CI/CD GIT METADATA PROBE         ")
    print("========================================")
    info = get_git_metadata()
    print(f"Inside Git Repo  : {info['is_git_repo']}")
    print(f"Active Branch    : {info['branch']}")
    print(f"Latest Commit SHA: {info['commit']}")
    print("========================================")
