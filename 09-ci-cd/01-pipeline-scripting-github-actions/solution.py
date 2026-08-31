"""
Lesson 01 (Module 09): Solution — Pipeline Step Output Exporter
"""
import os

def export_ci_output(key: str, value: str):
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")
        print(f"[CI/CD] Exported to $GITHUB_OUTPUT -> {key}={value}")
    else:
        print(f"[LOCAL RUNNER] Exported -> {key}={value}")

if __name__ == "__main__":
    print("========================================")
    print("      GITHUB ACTIONS OUTPUT TEST        ")
    print("========================================")
    export_ci_output("status", "PASSED")
    export_ci_output("release_version", "v2.4.0")
    print("========================================")
