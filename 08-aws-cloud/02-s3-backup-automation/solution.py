"""
Lesson 02 (Module 08): Solution — S3 Artifact Retention Auditor
"""
import time
from typing import List, Dict, Any

def audit_s3_retention(bucket_name: str, max_age_days: int = 30) -> List[Dict[str, Any]]:
    stale_objects = []
    cutoff_epoch = time.time() - (max_age_days * 86400)
    
    try:
        import boto3
        s3 = boto3.client("s3")
        paginator = s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get("Contents", []):
                last_mod_epoch = obj["LastModified"].timestamp()
                if last_mod_epoch < cutoff_epoch:
                    age_days = round((time.time() - last_mod_epoch) / 86400, 1)
                    stale_objects.append({
                        "key": obj["Key"],
                        "size_mb": round(obj["Size"] / (1024 ** 2), 2),
                        "age_days": age_days
                    })
    except Exception as err:
        print(f"[*] Simulation Mode (AWS offline: {err})")
        stale_objects = [
            {"key": "builds/v1.0.0-rc1.tar.gz", "size_mb": 145.2, "age_days": 48.5},
            {"key": "db_dumps/2026-06-15-backup.sql", "size_mb": 850.0, "age_days": 76.2}
        ]
        
    return stale_objects

if __name__ == "__main__":
    print("========================================")
    print("      S3 STALE OBJECT RETENTION AUDIT   ")
    print("========================================")
    results = audit_s3_retention("company-releases-bucket", max_age_days=30)
    print(f"Stale Objects Found: {len(results)}\n")
    for r in results:
        print(f"[STALE] Key: {r['key']:<35} | Size: {r['size_mb']:>7.2f} MB | Age: {r['age_days']} days")
    print("========================================")
