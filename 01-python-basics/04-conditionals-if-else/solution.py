"""
Lesson 04: Solution — CI/CD Deployment Gatekeeper
"""

def can_deploy(env, user_role, tests_passed, cve_critical_count):
    print(f"[*] Gating Check for Env: [{env}], Role: [{user_role}]")
    
    # 1. Fundamental Quality & Security Gates
    if not tests_passed:
        print("    [BLOCKED] Automated test suite did not pass.")
        return False
        
    if cve_critical_count > 0:
        print(f"    [BLOCKED] Security vulnerability gate tripped: {cve_critical_count} critical CVE(s).")
        return False
        
    # 2. Environment Specific Role Authorization
    if env.lower() == "production":
        if user_role in ["admin", "release-engineer"]:
            print("    [APPROVED] Authorized for Production deployment.")
            return True
        else:
            print(f"    [BLOCKED] Role '{user_role}' lacks Production deployment permissions.")
            return False
            
    elif env.lower() == "staging":
        if user_role in ["admin", "release-engineer", "developer"]:
            print("    [APPROVED] Authorized for Staging deployment.")
            return True
        else:
            print(f"    [BLOCKED] Role '{user_role}' is not authorized for Staging.")
            return False
            
    else:
        print(f"    [BLOCKED] Target environment '{env}' is unknown.")
        return False

if __name__ == "__main__":
    print("========================================")
    print("       DEPLOYMENT GATE AUDIT            ")
    print("========================================")
    r1 = can_deploy("production", "admin", True, 0)
    print(f"Outcome: Allowed = {r1}\n")
    
    r2 = can_deploy("production", "developer", True, 0)
    print(f"Outcome: Allowed = {r2}\n")
    
    r3 = can_deploy("staging", "developer", True, 1)
    print(f"Outcome: Allowed = {r3}\n")
    print("========================================")
