"""
Lesson 04 (Module 02): Exercise — Cloud Credential Validator

Task:
Write a function `load_aws_credentials()`:
1. Reads `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.
2. If `AWS_DEFAULT_REGION` is not set, default to `"us-east-1"`.
3. If either `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY` is missing or empty, raise a `ValueError` with a clear explanation.
4. Returns a dictionary with the credentials, with the secret key securely masked:
   `{"access_key": "AKIA...", "masked_secret": "wJal...****", "region": "us-east-1"}`
5. Handle exceptions and print an audit summary.
"""
import os

# TODO: Implement load_aws_credentials function

if __name__ == "__main__":
    pass
