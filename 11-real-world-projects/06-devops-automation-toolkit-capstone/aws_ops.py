"""
Capstone Module: AWS FinOps & Cloud Operations
"""

def run_aws_audit(region="us-east-1"):
    print("=========================================")
    print("        AWS CLOUD FINOPS AUDITOR         ")
    print("=========================================")
    print(f"Region: {region}\n")
    
    try:
        import boto3
        ec2 = boto3.client("ec2", region_name=region)
        vols = ec2.describe_volumes(Filters=[{"Name": "status", "Values": ["available"]}]).get("Volumes", [])
        print(f"Unattached EBS Volumes Found: {len(vols)}")
        for v in vols:
            print(f"  - Orphan: {v['VolumeId']} ({v['Size']} GB {v['VolumeType']})")
    except Exception as err:
        print(f"[*] Simulation Mode (AWS SDK offline: {err})")
        print("  - [ORPHAN VOL] vol-0123456789 (250 GB gp3) -> Est Waste: $20.00/mo")
        print("  - [IDLE EIP]   54.210.45.12   (No Instance) -> Est Waste: $3.65/mo")
        print("-----------------------------------------")
        print("ESTIMATED MONTHLY SAVINGS: $23.65 / month")
        
    print("=========================================")
