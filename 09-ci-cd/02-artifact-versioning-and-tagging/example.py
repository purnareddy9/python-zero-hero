"""
Lesson 02 (Module 09): Semantic Versioning and Automated Git Tagging
Example Script: Automated SemVer Release Calculator
"""
import re

def compute_next_semver(current_tag, commit_messages):
    print("========================================")
    print("      AUTOMATED SEMVER RELEASE ENGINE   ")
    print("========================================")
    print(f"Current Base Tag: {current_tag}")
    print(f"Commits to Audit: {len(commit_messages)}\n")
    
    match = re.match(r"^v?(\d+)\.(\d+)\.(\d+)$", current_tag.strip())
    if not match:
        raise ValueError(f"Invalid SemVer tag: '{current_tag}'")
        
    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))
    
    bump_type = "patch"
    
    for msg in commit_messages:
        msg_lower = msg.lower()
        if "breaking change" in msg_lower or "breaking:" in msg_lower:
            bump_type = "major"
            break
        elif msg_lower.startswith("feat:") or "feature:" in msg_lower:
            if bump_type != "major":
                bump_type = "minor"
                
    if bump_type == "major":
        next_tag = f"v{major + 1}.0.0"
    elif bump_type == "minor":
        next_tag = f"v{major}.{minor + 1}.0"
    else:
        next_tag = f"v{major}.{minor}.{patch + 1}"
        
    print("Analyzed Commits:")
    for m in commit_messages:
        print(f"  - {m}")
        
    print("----------------------------------------")
    print(f"Detected Bump Type : {bump_type.upper()}")
    print(f"Calculated Next Tag: {next_tag}")
    print("========================================")
    return next_tag

if __name__ == "__main__":
    recent_commits = [
        "docs: update deployment architecture diagram",
        "fix: resolve connection timeout in redis pool",
        "feat: add Apple Pay checkout support"
    ]
    compute_next_semver("v1.4.2", recent_commits)
