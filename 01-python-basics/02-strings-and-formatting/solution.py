"""
Lesson 02: Solution — Connection String Parser
"""

raw_entry = "   redis-cluster-01.internal.corp:6379/tcp   \n"

# 1. Clean the string
cleaned = raw_entry.strip()

# 2. Split host from the rest (port/protocol)
host_part, port_proto_part = cleaned.split(":")

# 3. Split port and protocol
port_str, protocol_str = port_proto_part.split("/")

# 4. Format & cast types
hostname = host_part
port = int(port_str)
protocol = protocol_str.upper()

# 5. Output summary
print("========================================")
print("     REDIS ENDPOINT CONFIGURATION       ")
print("========================================")
print(f"Target Host : {hostname}")
print(f"Target Port : {port} (Type: {type(port).__name__})")
print(f"Protocol    : {protocol}")
print(f"URI Scheme  : {protocol.lower()}://{hostname}:{port}")
print("========================================")
