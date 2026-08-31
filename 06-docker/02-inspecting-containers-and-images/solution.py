"""
Lesson 02 (Module 06): Solution — Container Environment Variable Parser
"""
from typing import List, Dict

raw_env_list = [
    "PORT=8080",
    "DB_HOST=10.0.0.15",
    "ENABLE_TLS=true",
    "DEBUG=false",
    "DB_NAME=production_db",
    "INVALID_ENTRY_WITHOUT_EQUALS",
    "REDIRECT_URI=https://app.net/callback?client=1&scope=all"
]

def parse_container_env_vars(env_list: List[str]) -> Dict[str, str]:
    env_map = {}
    for item in env_list:
        if "=" in item:
            key, val = item.split("=", 1)
            env_map[key] = val
    return env_map

if __name__ == "__main__":
    print("========================================")
    print("      CONTAINER ENV MAPPING AUDIT       ")
    print("========================================")
    parsed = parse_container_env_vars(raw_env_list)
    print(f"Total Valid Variables Extracted: {len(parsed)}\n")
    for k, v in parsed.items():
        print(f"  {k:<16} = {v}")
    print("========================================")
