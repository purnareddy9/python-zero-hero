"""
Lesson 04 (Module 05): Exercise — Semantic Version Validator & Tag Parser

Task:
Write a function `parse_git_release_tag(tag: str)`:
1. Validates whether `tag` is a valid semantic version (e.g. `v1.2.3`, `v10.4.0`, `1.0.0`).
2. Pattern rules:
   - Starts with an optional `v`.
   - Has `MAJOR.MINOR.PATCH` where each component is an integer.
3. If valid, return a dictionary with the extracted numbers:
   `{"valid": True, "major": 1, "minor": 2, "patch": 3}`
4. If invalid (e.g. `v1.2`, `beta-release`, `latest`), return:
   `{"valid": False}`
"""
import re

# TODO: Implement parse_git_release_tag function

if __name__ == "__main__":
    pass
