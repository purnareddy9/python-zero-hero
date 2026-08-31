"""
Lesson 02 (Module 09): Solution — Patch Version Bumper
"""
import re

def bump_patch_version(current_tag: str) -> str:
    match = re.match(r"^(v?)(\d+)\.(\d+)\.(\d+)$", current_tag.strip())
    if not match:
        raise ValueError(f"Invalid semantic version tag '{current_tag}'")
        
    prefix = match.group(1)
    major = int(match.group(2))
    minor = int(match.group(3))
    patch = int(match.group(4))
    
    return f"{prefix}{major}.{minor}.{patch + 1}"

if __name__ == "__main__":
    print("========================================")
    print("      PATCH VERSION BUMP TEST           ")
    print("========================================")
    test_tags = ["v1.0.4", "2.14.9", "v0.1.0"]
    for t in test_tags:
        bumped = bump_patch_version(t)
        print(f"Current: {t:<10} -> Next Patch: {bumped}")
    print("========================================")
