"""
Lesson 02: Strings and Formatting
Example Script: Log Line Sanitizer and Docker Tag Generator
"""

# 1. Parsing a raw log entry from standard input / file
raw_syslog_line = "  192.168.1.50 - - [31/Aug/2026] \"GET /api/v1/health HTTP/1.1\" 503 1420 \n"

# Clean up whitespace and newlines
clean_line = raw_syslog_line.strip()
tokens = clean_line.split(" ")

client_ip = tokens[0]
http_method = tokens[5].replace('"', '')
endpoint = tokens[6]
status_code = tokens[8]

print("========================================")
print("           LOG ENTRY PARSER             ")
print("========================================")
print(f"Client IP   : {client_ip}")
print(f"HTTP Request: {http_method} {endpoint}")
print(f"HTTP Status : {status_code}")

# 2. Constructing a Docker Image Repository URI
registry = "registry.internal.net"
service = "payment-gateway"
git_branch = "feature/checkout-fix"
git_sha = "a1b2c3d"

# Sanitize branch name for Docker tag (slashes not allowed in tags)
sanitized_branch = git_branch.replace("/", "-")
docker_tag = f"{registry}/{service}:{sanitized_branch}-{git_sha}"

print(f"Docker Image: {docker_tag}")
print("========================================")
