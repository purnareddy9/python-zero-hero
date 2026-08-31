"""
Lesson 01 (Module 09): Python in CI/CD: GitHub Actions, GitLab CI, and Jenkins
Example Script: CI/CD Monorepo Change Evaluator & Pipeline Gatekeeper
"""
import os

def evaluate_monorepo_pipeline(modified_files):
    print("========================================")
    print("     CI/CD MONOREPO BUILD EVALUATOR     ")
    print("========================================")
    
    git_sha = os.environ.get("GITHUB_SHA", "a1b2c3d4e5f6")[:7]
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    
    print(f"Pipeline Branch : {branch}")
    print(f"Commit Short SHA: {git_sha}")
    print(f"Modified Files  : {len(modified_files)}\n")
    
    services_to_build = set()
    for filepath in modified_files:
        if filepath.startswith("services/auth/"):
            services_to_build.add("auth-service")
        elif filepath.startswith("services/payment/"):
            services_to_build.add("payment-service")
        elif filepath.startswith("services/frontend/"):
            services_to_build.add("frontend-web")
        elif filepath.startswith("common/"):
            services_to_build.update(["auth-service", "payment-service", "frontend-web"])
            
    print(f"Services Requiring Build ({len(services_to_build)}):")
    for svc in sorted(services_to_build):
        print(f"  [TRIGGER BUILD] -> {svc}")
        
    gh_output_path = os.environ.get("GITHUB_OUTPUT")
    if gh_output_path:
        with open(gh_output_path, "a", encoding="utf-8") as f:
            f.write(f"build_count={len(services_to_build)}\n")
            f.write(f"services_json={list(services_to_build)}\n")
        print(f"\n[+] Successfully exported build parameters to $GITHUB_OUTPUT")
        
    print("========================================")
    return list(services_to_build)

if __name__ == "__main__":
    sample_diff = [
        "services/payment/api.py",
        "services/payment/requirements.txt",
        "README.md"
    ]
    evaluate_monorepo_pipeline(sample_diff)
