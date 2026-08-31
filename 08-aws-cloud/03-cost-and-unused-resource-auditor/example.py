"""
Lesson 03 (Module 08): Cloud Cost Optimization
Example Script: AWS FinOps Orphan Resource & Cost Waste Auditor
"""

def audit_wasted_cloud_resources(region="us-east-1"):
    print("========================================")
    print("     AWS CLOUD FINOPS & WASTE AUDITOR   ")
    print("========================================")
    print(f"Auditing Region: {region}\n")
    
    EBS_GP3_PER_GB_MONTH = 0.08
    IDLE_EIP_PER_MONTH = 3.65
    
    try:
        import boto3
        ec2 = boto3.client("ec2", region_name=region)
        
        vol_resp = ec2.describe_volumes(Filters=[{"Name": "status", "Values": ["available"]}])
        unattached_volumes = vol_resp.get("Volumes", [])
        
        eip_resp = ec2.describe_addresses()
        idle_eips = [
            a for a in eip_resp.get("Addresses", [])
            if "InstanceId" not in a and "NetworkInterfaceId" not in a
        ]
        
    except Exception as err:
        print(f"[*] Simulation Mode (AWS credentials/SDK offline: {err})\n")
        unattached_volumes = [
            {"VolumeId": "vol-0123456789abcdef0", "Size": 250, "VolumeType": "gp3"},
            {"VolumeId": "vol-0fedcba9876543210", "Size": 500, "VolumeType": "gp3"}
        ]
        idle_eips = [
            {"PublicIp": "54.210.45.12", "AllocationId": "eipalloc-0112233"},
            {"PublicIp": "34.195.88.90", "AllocationId": "eipalloc-0445566"}
        ]
        
    total_unattached_gb = sum(v["Size"] for v in unattached_volumes)
    ebs_monthly_waste = total_unattached_gb * EBS_GP3_PER_GB_MONTH
    eip_monthly_waste = len(idle_eips) * IDLE_EIP_PER_MONTH
    total_waste = ebs_monthly_waste + eip_monthly_waste
    
    print("1. Unattached EBS Volumes (Storage Waste):")
    for v in unattached_volumes:
        cost = v["Size"] * EBS_GP3_PER_GB_MONTH
        print(f"  [ORPHAN] ID: {v['VolumeId']} | Size: {v['Size']:>4} GB ({v['VolumeType']}) | Est: ${cost:.2f}/mo")
        
    print(f"\n2. Unassociated Idle Elastic IPs (IPv4 Waste):")
    for ip in idle_eips:
        print(f"  [IDLE]   IP: {ip['PublicIp']:<15} | Alloc: {ip['AllocationId']} | Est: ${IDLE_EIP_PER_MONTH:.2f}/mo")
        
    print("----------------------------------------")
    print(f"Total Unattached EBS Storage: {total_unattached_gb} GB")
    print(f"Total Idle Elastic IPs      : {len(idle_eips)}")
    print(f"ESTIMATED MONTHLY SAVINGS   : ${total_waste:.2f} / month")
    print("========================================")

if __name__ == "__main__":
    audit_wasted_cloud_resources()
