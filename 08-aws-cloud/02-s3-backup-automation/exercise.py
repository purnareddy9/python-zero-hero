"""
Lesson 02 (Module 08): Exercise — S3 Artifact Retention Auditor

Task:
Write a function `audit_s3_retention(bucket_name: str, max_age_days: int = 30)`:
1. Connects to `boto3.client('s3')`.
2. Lists objects in `bucket_name` using `s3.list_objects_v2()`.
3. Identifies objects with `LastModified` older than `max_age_days`.
4. Returns a list of stale objects: `[{"key": "...", "size_mb": 12.4, "age_days": 45}, ...]`.
5. Handles offline SDK with simulated mock data.
"""

# TODO: Implement audit_s3_retention function

if __name__ == "__main__":
    pass
