"""
Lesson 02: Exercise — Connection String Parser

Task:
You are given a raw configuration line:
`raw_entry = "   redis-cluster-01.internal.corp:6379/tcp   \n"`

1. Strip the leading/trailing spaces and newline.
2. Extract the hostname: `redis-cluster-01.internal.corp`
3. Extract the port as an integer: `6379`
4. Extract the protocol in uppercase: `TCP`
5. Print an audit summary using f-strings.
"""

raw_entry = "   redis-cluster-01.internal.corp:6379/tcp   \n"

# TODO: Implement string cleaning and extraction logic here
