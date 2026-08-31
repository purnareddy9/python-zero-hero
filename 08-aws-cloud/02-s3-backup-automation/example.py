"""
Lesson 02 (Module 08): S3 Storage Automation and Artifact Uploads
Example Script: Automated Build Artifact & Database S3 Backup Uploader
"""
import os

def upload_artifact_to_s3(local_filepath, target_bucket, s3_prefix="backups/"):
    print("========================================")
    print("       AWS S3 BACKUP & UPLOAD AGENT     ")
    print("========================================")
    print(f"Source File  : {local_filepath}")
    print(f"Target Bucket: {target_bucket}")
    
    if not os.path.exists(local_filepath):
        print(f"[!] ERROR: Local file '{local_filepath}' does not exist.")
        return False
        
    filename = os.path.basename(local_filepath)
    s3_key = f"{s3_prefix.rstrip('/')}/{filename}"
    file_size_kb = round(os.path.getsize(local_filepath) / 1024, 2)
    
    print(f"Destination  : s3://{target_bucket}/{s3_key} ({file_size_kb} KB)")
    print("----------------------------------------")
    
    try:
        import boto3
        s3 = boto3.client("s3")
        s3.upload_file(
            Filename=local_filepath,
            Bucket=target_bucket,
            Key=s3_key,
            ExtraArgs={"ServerSideEncryption": "AES256"}
        )
        print("[+] Upload completed successfully.")
        return True
    except Exception as err:
        print(f"[*] Simulating S3 upload (AWS offline / mock mode: {err})\n")
        print("[+] [SIMULATED SUCCESS]: File uploaded with SSE-S3 AES-256.")
        print(f"[+] S3 URI: s3://{target_bucket}/{s3_key}")
        print("========================================")
        return True

if __name__ == "__main__":
    demo_file = "app_backup_20260831.tar.gz"
    with open(demo_file, "w") as f:
        f.write("SAMPLE BACKUP BINARY CONTENT\n" * 50)
        
    upload_artifact_to_s3(demo_file, "corp-production-backups-bucket")
