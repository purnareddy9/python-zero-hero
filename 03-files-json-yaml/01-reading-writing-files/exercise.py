"""
Lesson 01 (Module 03): Exercise — Audit Logger

Task:
Write a function `append_audit_log(filepath: str, user: str, action: str, status: str = "SUCCESS")`:
1. Constructs an entry in format: `[YYYY-MM-DD HH:MM:SS] USER: <user> | ACTION: <action> | STATUS: <status>\n`
2. Appends the line safely to `filepath` using `with open(..., "a")`.
3. Handles `PermissionError` gracefully.
4. Returns `True` on success, `False` on error.
"""
import time

# TODO: Implement append_audit_log function

if __name__ == "__main__":
    pass
