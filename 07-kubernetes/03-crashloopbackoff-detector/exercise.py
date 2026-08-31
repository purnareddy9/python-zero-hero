"""
Lesson 03 (Module 07): Exercise — Container Exit Code Diagnostic Engine

Task:
Write a diagnostic function `diagnose_container_exit(exit_code: int) -> dict`:
Given an integer exit code from a terminated container:
- Return a dictionary:
  `{"exit_code": exit_code, "severity": "CRITICAL" | "WARNING" | "INFO", "diagnosis": str, "recommended_action": str}`

Rules:
- `0`: Severity "INFO", "Graceful process completion", "None required"
- `1` or `2`: Severity "CRITICAL", "Application crash / unhandled exception", "Check application stack trace logs"
- `137`: Severity "CRITICAL", "OOMKilled (Out of Memory - SIGKILL)", "Increase container memory limits in spec"
- `143`: Severity "WARNING", "Graceful SIGTERM received", "Verify if termination was intended"
- Any other code: Severity "WARNING", "Non-standard exit code", "Inspect container stderr logs"
"""

# TODO: Implement diagnose_container_exit function

if __name__ == "__main__":
    pass
