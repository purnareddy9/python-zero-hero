"""
Lesson 04: Exercise — CI/CD Deployment Gatekeeper

Task:
Write a function `can_deploy(env, user_role, tests_passed, cve_critical_count)` that returns:
- `True` if deployment is allowed.
- `False` if deployment must be blocked.

Rules:
1. If `tests_passed` is False -> REJECT immediately (reason: "Tests failed").
2. If `cve_critical_count` > 0 -> REJECT immediately (reason: "Critical security vulnerabilities detected").
3. For `env == "production"`:
   - Only allowed if `user_role == "release-engineer"` or `user_role == "admin"`.
4. For `env == "staging"`:
   - Allowed for `"developer"`, `"release-engineer"`, or `"admin"`.
5. Any other environment -> REJECT (reason: "Invalid environment").
"""

def can_deploy(env, user_role, tests_passed, cve_critical_count):
    # TODO: Implement conditional gating rules
    pass

if __name__ == "__main__":
    # Test cases:
    print("Test 1 (Prod Admin, Clean):", can_deploy("production", "admin", True, 0)) # Should be True
    print("Test 2 (Prod Dev, Clean):", can_deploy("production", "developer", True, 0)) # Should be False
    print("Test 3 (Staging Dev, CVE=1):", can_deploy("staging", "developer", True, 1)) # Should be False
