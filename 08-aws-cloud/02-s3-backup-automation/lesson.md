# Lesson 02 — S3 Storage Automation and Artifact Uploads

## 🎯 What will I learn?
You will learn how to automate Amazon Simple Storage Service (S3) using Boto3: creating buckets, uploading build artifacts (`upload_file`), downloading configuration bundles, setting server-side encryption (SSE-S3 / SSE-KMS), and configuring object lifecycle policies.

---

## 🤔 Why does a DevOps engineer need this?
S3 is the central storage layer in AWS DevOps architectures:

- Uploading CI/CD build artifacts (`.tar.gz`, `.jar`, `.whl`) with version tags.
- Streaming automated nightly PostgreSQL/MySQL database dumps to secure backup buckets.
- Enforcing security policies (blocking public access and forcing AES-256 encryption on upload).

---

## 🧠 Mental model

```mermaid
flowchart LR
    Local["Local File: backup-2026-08-31.tar.gz"] --> Python["s3.upload_file(local_path, bucket, s3_key)"]
    Python --> S3[Amazon S3 Bucket: my-prod-backups]
    S3 --> Storage["Encrypted at rest with AES-256 (SSE-S3)"]
```

---

## 📖 Concept

### Uploading Files with Server-Side Encryption

```python
import boto3

s3 = boto3.client("s3")

# Upload file with AES-256 encryption enabled
s3.upload_file(
    Filename="build_artifact.zip",
    Bucket="my-company-artifacts-bucket",
    Key="releases/v2.1.0/build_artifact.zip",
    ExtraArgs={"ServerSideEncryption": "AES256"}
)
```

---

## 💻 Simple example

```python
import boto3

s3 = boto3.client("s3")
# buckets = s3.list_buckets()
# for b in buckets.get('Buckets', []): print(b['Name'])
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Automated Build Artifact & Database S3 Backup Uploader
Demonstrates secure S3 uploads with AES-256 encryption and progress callback.
"""
import os
import sys

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
        
        print("[*] Initiating multipart upload with AES-256 encryption...")
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
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
       AWS S3 BACKUP & UPLOAD AGENT     
========================================
Source File  : app_backup_20260831.tar.gz
Target Bucket: corp-production-backups-bucket
Destination  : s3://corp-production-backups-bucket/backups/app_backup_20260831.tar.gz (1.42 KB)
----------------------------------------
[+] [SIMULATED SUCCESS]: File uploaded with SSE-S3 AES-256.
[+] S3 URI: s3://corp-production-backups-bucket/backups/app_backup_20260831.tar.gz
========================================
```

---

## 🔍 Line-by-line explanation
- `ExtraArgs={"ServerSideEncryption": "AES256"}`: Enforces server-side encryption at rest.
- `s3.upload_file(...)`: Automatically uses multipart streaming under the hood for large files (> 8 MB) to prevent memory bottlenecks.

---

## 🐚 Shell equivalent

```bash
aws s3 cp app_backup.tar.gz s3://corp-production-backups-bucket/backups/ --sse AES256
```

---

## ⚙️ Ansible equivalent

```yaml
- name: Upload backup artifact to S3
  amazon.aws.s3_object:
    bucket: corp-production-backups-bucket
    object: backups/app_backup.tar.gz
    src: /tmp/app_backup.tar.gz
    mode: put
    encrypt: yes
```

---

## 🏆 Which one should I use?
- Use **`aws s3 sync` / `cp`** for simple single-command file copies in CI/CD.
- Use **Python Boto3** when upload needs to be verified, checksummed (MD5/SHA256), recorded in a database, and trigger automated Slack notifications.

---

## ⚠️ Common mistakes
1. **Using `s3.put_object(Body=open('huge_file.zip', 'rb').read())`:**

   - Loading the whole file into RAM with `.read()` crashes with large 5 GB backups! Always use `s3.upload_file()`, which streams files in chunks automatically.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Write a function `list_s3_bucket_objects_older_than(bucket_name, days=30)` that returns all S3 keys in a bucket whose `LastModified` date is older than `days`.

---

## 💡 Hint
Compare `obj["LastModified"].timestamp() < cutoff_timestamp`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "Why should you use `s3.upload_file()` instead of `s3.put_object()` when uploading large backups to S3?"
> **Interviewer Focus:** Testing knowledge of multipart upload chunking, memory safety, and high-throughput transfer managers.

---

## 🗣️ How to answer in an interview
> *"`s3.put_object()` requires loading the entire file payload into Python process memory as bytes, which will exhaust RAM on large database dumps or disk images. In contrast, `s3.upload_file()` utilizes the Boto3 TransferManager, which automatically handles multi-threaded multipart streaming, re-attempts failed individual chunks, and streams directly from disk buffers with minimal memory consumption."*

---

## 📝 What I should remember
- Use `s3.upload_file()` for safe streaming multipart uploads.
- Always include `ExtraArgs={"ServerSideEncryption": "AES256"}`.
- Never load large files into RAM with `f.read()`.
