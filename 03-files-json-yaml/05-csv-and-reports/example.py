"""
Lesson 05 (Module 03): CSV and Audit Reports
Example Script: Multi-Cloud Infrastructure Security & Cost Audit CSV Exporter
"""
import csv
import os

def generate_compliance_csv_report(output_filepath="cloud_security_audit.csv"):
    print("========================================")
    print("     CLOUD SECURITY & COST AUDITOR      ")
    print("========================================")
    
    infrastructure_records = [
        {"resource_id": "i-0a1b2c3d4e", "resource_type": "EC2 Instance", "region": "us-east-1", "cost_monthly": 142.50, "is_encrypted": True, "status": "COMPLIANT"},
        {"resource_id": "vol-0998877665", "resource_type": "EBS Volume", "region": "us-east-1", "cost_monthly": 24.00, "is_encrypted": False, "status": "NON_COMPLIANT"},
        {"resource_id": "s3-client-backups", "resource_type": "S3 Bucket", "region": "eu-west-1", "cost_monthly": 85.20, "is_encrypted": True, "status": "COMPLIANT"},
        {"resource_id": "rds-postgres-prod", "resource_type": "RDS Instance", "region": "us-west-2", "cost_monthly": 450.00, "is_encrypted": True, "status": "COMPLIANT"}
    ]
    
    fieldnames = ["resource_id", "resource_type", "region", "cost_monthly", "is_encrypted", "status"]
    
    with open(output_filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(infrastructure_records)
        
    print(f"[+] Audit exported successfully to: {os.path.abspath(output_filepath)}")
    
    total_cost = sum(r["cost_monthly"] for r in infrastructure_records)
    non_compliant = [r for r in infrastructure_records if r["status"] == "NON_COMPLIANT"]
    
    print(f"Total Resources Audited: {len(infrastructure_records)}")
    print(f"Projected Monthly Spend: ${total_cost:.2f}")
    print(f"Non-Compliant Violations: {len(non_compliant)}")
    print("========================================")

if __name__ == "__main__":
    generate_compliance_csv_report()
