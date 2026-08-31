"""
Lesson 04 (Module 02): Environment Variables and Secrets Management
Example Script: CI/CD Pipeline Environment Pre-Flight Validator
"""
import os
import sys

def validate_pipeline_environment():
    print("========================================")
    print("     CI/CD ENVIRONMENT & SECRET AUDIT   ")
    print("========================================")
    
    # 1. Non-sensitive configuration (safe to log)
    environment = os.environ.get("ENVIRONMENT", "staging")
    region = os.environ.get("AWS_REGION", "us-east-1")
    build_id = os.environ.get("BUILD_ID", "local-dev-001")
    
    print(f"Target Environment: {environment}")
    print(f"Deployment Region : {region}")
    print(f"Pipeline Build ID : {build_id}")
    print("----------------------------------------")
    
    # 2. Mandatory Secret Validation (NEVER print raw secrets!)
    required_secrets = ["API_SECRET_KEY", "DATABASE_PASSWORD"]
    missing_secrets = []
    
    for secret_name in required_secrets:
        secret_val = os.environ.get(secret_name)
        if not secret_val:
            print(f"[MISSING] {secret_name:<20} (FAILED)")
            missing_secrets.append(secret_name)
        else:
            # Mask secret in logs for security audit
            masked = secret_val[:2] + "********" + secret_val[-2:] if len(secret_val) > 4 else "********"
            print(f"[LOADED]  {secret_name:<20} -> Masked: {masked}")
            
    print("========================================")
    if missing_secrets:
        print(f"[!] HALTING: Missing mandatory secrets: {missing_secrets}")
        return False
        
    print("[+] Environment pre-flight check passed. Proceeding with deployment.")
    return True

if __name__ == "__main__":
    os.environ["API_SECRET_KEY"] = "prod_secret_token_xyz987"
    is_valid = validate_pipeline_environment()
    sys.exit(0 if is_valid else 1)
