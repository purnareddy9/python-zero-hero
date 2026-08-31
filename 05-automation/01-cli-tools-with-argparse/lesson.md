# Lesson 01 — Building Professional CLI Automation Tools with `argparse`

## 🎯 What will I learn?
You will learn how to build enterprise-grade Command Line Interface (CLI) utilities using Python's standard `argparse` module: adding positional arguments, optional flags (`--env`, `--dry-run`, `--verbose`), subcommands (like `docker run` or `git commit`), help text generation (`--help`), and type validation.

---

## 🤔 Why does a DevOps engineer need this?
DevOps engineers build internal tools for development and operations teams:
- Deployer CLIs: `python deploy_tool.py --env prod --replicas 5 --dry-run`
- Multi-command maintenance tools: `python ops.py health`, `python ops.py disk --clean`, `python ops.py restart --service nginx`
- `argparse` automatically generates beautiful `--help` documentation and handles flag validation out of the box.

---

## 🧠 Mental model

```mermaid
flowchart LR
    User["$ python ops.py --env prod --dry-run"] --> Argparse["argparse.ArgumentParser()"]
    Argparse --> Parse["args.env = 'prod'<br/>args.dry_run = True"]
    Parse --> AutomationLogic["Execute deployment with safety guards"]
```

---

## 📖 Concept

### Anatomy of an `argparse` CLI Tool

```python
import argparse

parser = argparse.ArgumentParser(description="Production Microservice Deployment CLI")

# Positional Argument (Mandatory)
parser.add_argument("service", help="Name of the microservice to deploy")

# Optional Flags with defaults and choices
parser.add_argument("--env", choices=["dev", "staging", "prod"], default="staging", help="Target environment")
parser.add_argument("--replicas", type=int, default=3, help="Desired replica count")
parser.add_argument("--dry-run", action="store_true", help="Simulate execution without modifying infrastructure")

args = parser.parse_args()
print(f"Deploying {args.service} to {args.env} (Dry-Run: {args.dry_run})")
```

---

## 💻 Simple example

```python
import argparse

parser = argparse.ArgumentParser(description="Quick Host Check")
parser.add_argument("-H", "--host", required=True, help="Target Host IP/DNS")
parser.add_argument("-p", "--port", type=int, default=80, help="Port (default: 80)")

args = parser.parse_args()
print(f"Connecting to {args.host}:{args.port}")
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Multi-Environment Deployment & Maintenance CLI Tool
Demonstrates flags, boolean switches, subcommands, and automated help menus.
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="devops-deployer",
        description="🚀 Enterprise Multi-Cloud Deployment & Automation CLI",
        epilog="Example: python example.py payment-service --env production --replicas 5 --dry-run"
    )
    
    # Mandatory Positional Argument
    parser.add_argument("service_name", help="Name of the service / container to manage")
    
    # Optional Named Arguments
    parser.add_argument(
        "-e", "--env",
        choices=["development", "staging", "production"],
        default="staging",
        help="Target cloud deployment environment (default: staging)"
    )
    
    parser.add_argument(
        "-r", "--replicas",
        type=int,
        default=2,
        help="Number of container replicas to launch (default: 2)"
    )
    
    parser.add_argument(
        "--image-tag",
        default="v1.0.0",
        help="Docker image version tag (default: v1.0.0)"
    )
    
    # Boolean Switch (Flag present = True, absent = False)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate execution without modifying real infrastructure"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging output"
    )
    
    # Parse CLI inputs
    args = parser.parse_args()
    
    print("========================================")
    print("      DEVOPS DEPLOYMENT CLI EXECUTION   ")
    print("========================================")
    print(f"Target Service   : {args.service_name}")
    print(f"Environment      : {args.env}")
    print(f"Image Version    : {args.image_tag}")
    print(f"Desired Replicas : {args.replicas}")
    print(f"Dry-Run Mode     : {args.dry_run}")
    print(f"Verbose Logging  : {args.verbose}")
    print("----------------------------------------")
    
    if args.dry_run:
        print("[DRY-RUN] [SIMULATION ONLY] Plan: Would launch", args.replicas, "replicas of", args.service_name)
        print("[DRY-RUN] No infrastructure modified.")
    else:
        print(f"[ACTION] Applying Kubernetes deployment manifests for '{args.service_name}'...")
        print("[+] Deployment completed successfully.")
        
    print("========================================")

if __name__ == "__main__":
    main()
```

---

## 🖥️ Expected output

```text
$ python example.py auth-api --env production --replicas 4 --dry-run
========================================
      DEVOPS DEPLOYMENT CLI EXECUTION   
========================================
Target Service   : auth-api
Environment      : production
Image Version    : v1.0.0
Desired Replicas : 4
Dry-Run Mode     : True
Verbose Logging  : False
----------------------------------------
[DRY-RUN] [SIMULATION ONLY] Plan: Would launch 4 replicas of auth-api
[DRY-RUN] No infrastructure modified.
========================================
```

---

## 🔍 Line-by-line explanation
- `action="store_true"`: Flags like `--dry-run` or `--verbose` don't require values. If passed on CLI, `args.dry_run` evaluates to `True`; if omitted, it defaults to `False`.
- `choices=[...]`: Rejects invalid values immediately at parse time with an informative error message.
- `type=int`: Automatically converts the argument string to an integer, raising an error if a non-numeric string is provided.

---

## 🐚 Shell equivalent

```bash
# In Bash, parsing flags requires complex getopts:
while getopts "e:r:d" opt; do
  case ${opt} in
    e ) ENV=$OPTARG ;;
    r ) REPLICAS=$OPTARG ;;
    d ) DRY_RUN=true ;;
  esac
done
```
*Why Python is better:* `getopts` in Bash is difficult to write, does not support long flags (`--environment`, `--dry-run`), and cannot generate automatic `--help` menus.

---

## ⚙️ Ansible equivalent

Ansible CLI commands use standard flags (`ansible-playbook -i hosts site.yml -e "env=prod" --check`).

---

## 🏆 Which one should I use?
- Use **Python `argparse`** for all custom operational tools, infrastructure migration scripts, and multi-option team utilities.

---

## ⚠️ Common mistakes
1. **Using `sys.argv` indexing directly instead of `argparse`:**
   - Indexing `sys.argv` manually breaks if the user switches the order of flags or asks for `--help`.
2. **Forgetting `action="store_true"` for boolean flags:**
   - Without `store_true`, `parser.add_argument("--dry-run")` expects a value (`--dry-run true`), which confuses users.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Build a CLI tool `disk-auditor` that accepts a mandatory `--mount` path (e.g. `/` or `/var`), an optional `--threshold` integer (default: 80), and an optional `--notify-slack` boolean switch.

---

## 💡 Hint
Use `parser.add_argument("--mount", required=True)`, `parser.add_argument("--threshold", type=int, default=80)`, and `parser.add_argument("--notify-slack", action="store_true")`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "Why is `argparse` preferred over `sys.argv` or `getopt` when developing automation tooling for engineering teams?"
> **Interviewer Focus:** Testing developer experience (DX) awareness, error validation, and standard library best practices.

---

## 🗣️ How to answer in an interview
> *"`argparse` is the standard library framework for production-grade CLI tools. Unlike raw `sys.argv` indexing, `argparse` automatically handles POSIX flag syntax (short `-e` and long `--env`), generates built-in `--help` documentation, validates choices and data types (casting strings to integers), supports subcommands (like `git status` vs `git commit`), and provides descriptive error messages for missing parameters without writing manual validation boilerplate."*

---

## 📝 What I should remember
- Use `argparse.ArgumentParser(description=...)`.
- Use `action="store_true"` for toggle flags (`--dry-run`).
- Use `choices=[...]` to restrict inputs to valid options.
- Use `type=int` or `type=float` for automatic type validation.
