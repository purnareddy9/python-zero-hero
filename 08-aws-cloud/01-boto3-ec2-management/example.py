"""
Lesson 01 (Module 08): AWS Automation with Boto3: EC2 Instance Management
Example Script: Non-Prod EC2 Nightly Cost-Saver & Tag Auditor
"""

def audit_and_manage_ec2_instances(region="us-east-1", action="audit"):
    print("========================================")
    print("      AWS EC2 INSTANCE COST AUDITOR     ")
    print("========================================")
    print(f"Target AWS Region: {region}")
    print(f"Operational Mode : {action.upper()}\n")
    
    try:
        import boto3
        ec2 = boto3.client("ec2", region_name=region)
        
        filters = [
            {"Name": "tag:Environment", "Values": ["development", "dev", "staging"]},
            {"Name": "instance-state-name", "Values": ["running", "stopped"]}
        ]
        
        response = ec2.describe_instances(Filters=filters)
        reservations = response.get("Reservations", [])
        
        instances = []
        for res in reservations:
            for inst in res.get("Instances", []):
                name_tag = next((t["Value"] for t in inst.get("Tags", []) if t["Key"] == "Name"), "Unnamed")
                instances.append({
                    "id": inst["InstanceId"],
                    "name": name_tag,
                    "type": inst["InstanceType"],
                    "state": inst["State"]["Name"],
                    "ip": inst.get("PrivateIpAddress", "N/A")
                })
                
        print(f"Total Filtered Instances: {len(instances)}\n")
        for i in instances:
            status_tag = "[RUNNING]" if i["state"] == "running" else "[STOPPED]"
            print(f"{status_tag:<10} ID: {i['id']} | Type: {i['type']:<10} | Name: {i['name']:<20} | IP: {i['ip']}")
            
    except Exception as err:
        print(f"[*] Simulating AWS EC2 inventory (AWS credentials/SDK offline: {err})\n")
        mock_instances = [
            ("i-0a11223344", "dev-auth-api", "t3.medium", "running", "10.0.1.45"),
            ("i-0b55667788", "staging-redis", "t3.small", "running", "10.0.1.80"),
            ("i-0c99001122", "dev-test-runner", "t3.micro", "stopped", "10.0.2.12")
        ]
        for i_id, name, itype, state, ip in mock_instances:
            tag = f"[{state.upper()}]"
            print(f"{tag:<10} ID: {i_id} | Type: {itype:<10} | Name: {name:<20} | IP: {ip}")
        print("\n[+] [SIMULATED ACTION] Cost Saver: Would stop 2 running dev instances at 7 PM.")
        
    print("========================================")

if __name__ == "__main__":
    audit_and_manage_ec2_instances("us-east-1", action="audit")
