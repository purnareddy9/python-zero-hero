"""
Lesson 01 (Module 08): Exercise — Mandatory Tag Compliance Auditor

Task:
Write a function `audit_ec2_tag_compliance(region="us-east-1", required_tags=("Environment", "Owner"))`:
1. Queries all EC2 instances in the region using `boto3.client('ec2')`.
2. Inspects the `Tags` list on each instance.
3. Identifies non-compliant instances that are missing ANY of the `required_tags`.
4. Returns a list of non-compliant instances:
   `[{"id": "i-...", "name": "...", "missing_tags": ["Owner"]}, ...]`
5. Handles offline SDK gracefully by returning a simulated mock list.
"""

# TODO: Implement audit_ec2_tag_compliance function

if __name__ == "__main__":
    pass
