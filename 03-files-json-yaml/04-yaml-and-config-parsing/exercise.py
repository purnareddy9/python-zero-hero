"""
Lesson 04 (Module 03): Exercise — Docker Compose Hardener

Task:
You are given a raw Docker Compose configuration string:
`compose_yaml = '''
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
  worker:
    image: python-worker:latest
'''`

Write a function `harden_compose_spec(yaml_str)` that:
1. Parses the YAML using `yaml.safe_load()`.
2. Loops through every service under `services`.
3. Adds `restart: always` to all services.
4. If the service image tag is `:latest`, replace `:latest` with `:stable`.
5. Dumps the updated YAML and prints it cleanly.
"""
import yaml

# TODO: Implement Docker Compose spec hardener using PyYAML

if __name__ == "__main__":
    pass
