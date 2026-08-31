"""
Project 03: Exercise — Automated Disk Remediation Purger

Task:
Write a function `auto_remediate_disk(target_dir: str, usage_pct: float, threshold: float = 90.0)`:
1. If `usage_pct >= threshold`:
   - Scan `target_dir` for old `.gz` or `.old` files.
   - Delete matched files and calculate total bytes freed.
   - Print `"[REMEDIATION] Purged X bytes to recover disk capacity."`
   - Return `True`.
2. If `usage_pct < threshold`:
   - Print `"[NORMAL] Disk space within parameters. No remediation needed."`
   - Return `False`.
"""

# TODO: Implement auto_remediate_disk function

if __name__ == "__main__":
    pass
