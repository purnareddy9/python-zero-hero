"""
Lesson 01 (Module 10): Troubleshooting Common Python Errors in DevOps
Example Script: Defensive Exception Handling & Triage Engine
"""

def safe_config_lookup(config_dict, key, default="DEFAULT_VAL"):
    try:
        return config_dict[key]
    except KeyError:
        print(f"[*] KeyError caught: '{key}' not in config. Falling back to '{default}'.")
        return default

def safe_file_reader(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"[!] FileNotFoundError: '{filepath}' does not exist.")
        return None
    except PermissionError:
        print(f"[!] PermissionError: Insufficient privileges to read '{filepath}'.")
        return None

if __name__ == "__main__":
    print("========================================")
    print("      DEVOPS ERROR TRIAGE TEST          ")
    print("========================================")
    
    dummy_config = {"env": "prod", "cluster": "k8s-east"}
    region = safe_config_lookup(dummy_config, "aws_region", "us-east-1")
    print(f"Resolved Region: {region}\n")
    
    content = safe_file_reader("/etc/non_existent_secret.conf")
    print(f"File Content Result: {content}")
    print("========================================")
