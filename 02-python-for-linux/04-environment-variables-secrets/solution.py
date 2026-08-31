"""
Lesson 04 (Module 02): Solution — Cloud Credential Validator
"""
import os
from typing import Dict, Any

def load_aws_credentials() -> Dict[str, Any]:
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
    
    missing = []
    if not access_key:
        missing.append("AWS_ACCESS_KEY_ID")
    if not secret_key:
        missing.append("AWS_SECRET_ACCESS_KEY")
        
    if missing:
        raise ValueError(f"Missing mandatory AWS credential environment variables: {', '.join(missing)}")
        
    # Mask secret key for audit reporting
    masked_secret = secret_key[:4] + "..." + "*" * 8
    
    return {
        "access_key": access_key,
        "masked_secret": masked_secret,
        "region": region
    }

if __name__ == "__main__":
    print("========================================")
    print("      AWS CREDENTIAL PRE-FLIGHT CHECK   ")
    print("========================================")
    
    # 1. Simulate setting valid credentials
    os.environ["AWS_ACCESS_KEY_ID"] = "AKIAIOSFODNN7EXAMPLE"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-1"
    
    try:
        creds = load_aws_credentials()
        print("[+] Credentials successfully loaded from environment:")
        print(f"    Access Key : {creds['access_key']}")
        print(f"    Secret Key : {creds['masked_secret']}")
        print(f"    Region     : {creds['region']}")
    except ValueError as err:
        print(f"[!] Authentication Error: {err}")
        
    print("========================================")
