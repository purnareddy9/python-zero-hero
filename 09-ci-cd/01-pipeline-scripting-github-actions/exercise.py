"""
Lesson 01 (Module 09): Exercise — Pipeline Step Output Exporter

Task:
Write a function `export_ci_output(key: str, value: str)`:
1. Checks if `GITHUB_OUTPUT` environment variable is defined.
2. If defined, appends `{key}={value}\n` to that file path safely.
3. If `GITHUB_OUTPUT` is NOT defined (e.g. running on local laptop), print `[LOCAL] Exported {key}={value}`.
4. Test exporting `status=PASSED` and `release_version=v2.4.0`.
"""
import os

# TODO: Implement export_ci_output function

if __name__ == "__main__":
    pass
