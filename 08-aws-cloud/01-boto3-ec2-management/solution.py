"""
Lesson 01 (Module 08): Solution — Mandatory Tag Compliance Auditor
"""
from typing import List, Dict, Any, Tuple

def audit_ec2_tag_compliance(region: str = "us-east-1", required_tags: Tuple[str, ...] = ("Environment", "Owner")) -> List[Dict[str, Any]]:
    non_compliant = []
    try:
        import boto3
        ec2 = boto3.client("ec2", region_name=region)
        response = ec2.describe_instances()
        for res in response.get("Reservations", []):
            for inst in res.get("Instances", []):
                tags = inst.get("Tags", [])
                tag_keys = {t["Key"] for t in tags}
                name_tag = next((t["Value"] for t in tags if t["Key"] == "Name"), "Unnamed")
                missing = [req for req in required_tags if req not in tag_keys]
                if missing:
                    non_compliant.append({
                        "id": inst["InstanceId"],
                        "name": name_tag,
                        "missing_tags": missing
                    })
    except Exception as err:
        print(f"[*] Simulation Mode (AWS SDK offline: {err})")
        non_compliant = [
            {"id": "i-0998877665", "name": "temp-analytics-worker", "missing_tags": ["Owner"]},
            {"id": "i-0112233445", "name": "legacy-vpn-gateway", "missing_tags": ["Environment", "Owner"]}
        ]
        
    return non_compliant

if __name__ == "__main__":
    print("========================================")
    print("     AWS TAG GOVERNANCE COMPLIANCE      ")
    print("========================================")
    violations = audit_ec2_tag_compliance()
    print(f"Total Tag Policy Violations Found: {len(violations)}\n")
    for v in violations:
        print(f"[NON-COMPLIANT] ID: {v['id']} ({v['name']:<20})")
        print(f"                Missing Tags: {', '.join(v['missing_tags'])}\n")
    print("========================================")
