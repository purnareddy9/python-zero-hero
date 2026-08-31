"""
Lesson 02 (Module 06): Exercise — Container Environment Variable Parser

Task:
You are inspecting a container and retrieve its environment configuration array:
`raw_env_list = ["PORT=8080", "DB_HOST=10.0.0.15", "ENABLE_TLS=true", "DEBUG=false", "DB_NAME=production_db"]`

Write a function `parse_container_env_vars(env_list)`:
1. Converts the list of `"KEY=VAL"` strings into a clean dictionary `{"PORT": "8080", "DB_HOST": "10.0.0.15", ...}`.
2. If an entry does not contain an `=`, skip it.
3. If an entry has multiple `=` signs (e.g. `URL=https://app.net?q=1`), split ONLY on the first `=` sign.
4. Return the parsed dictionary.
"""

# TODO: Implement parse_container_env_vars function

if __name__ == "__main__":
    pass
