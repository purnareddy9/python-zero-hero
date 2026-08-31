"""
Lesson 04 (Module 05): Solution — Semantic Version Validator & Tag Parser
"""
import re
from typing import Dict, Any

SEMVER_PATTERN = re.compile(r"^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)$")

def parse_git_release_tag(tag: str) -> Dict[str, Any]:
    match = SEMVER_PATTERN.match(tag.strip())
    if match:
        return {
            "valid": True,
            "raw_tag": tag,
            "major": int(match.group("major")),
            "minor": int(match.group("minor")),
            "patch": int(match.group("patch"))
        }
    return {"valid": False, "raw_tag": tag}

if __name__ == "__main__":
    test_tags = ["v1.4.2", "2.10.0", "v1.2", "release-candidate", "v0.9.15", "latest"]
    
    print("========================================")
    print("      GIT RELEASE TAG SEMVER AUDIT      ")
    print("========================================")
    for tag in test_tags:
        res = parse_git_release_tag(tag)
        if res["valid"]:
            print(f"[VALID]   Tag '{res['raw_tag']:<15}' -> Major: {res['major']}, Minor: {res['minor']}, Patch: {res['patch']}")
        else:
            print(f"[INVALID] Tag '{res['raw_tag']:<15}' -> (Rejected)")
    print("========================================")
