# Lesson 09 — Modules, Imports, Pip, and Virtual Environments in DevOps

## 🎯 What will I learn?
You will learn how Python organizes code into **Modules** and **Packages**, how to import built-in and third-party libraries, and why isolated **Virtual Environments (`venv`)** are critical in Linux servers and CI/CD runners to prevent package conflicts.

---

## 🤔 Why does a DevOps engineer need this?
1. **Linux System Python Protection:** Modifying the system Python (`/usr/bin/python3`) on Ubuntu or RHEL can break essential OS tools like `apt`, `yum`, or `dnf` (Debian PEP 668: *externally-managed-environment* error).
2. **Deterministic CI/CD Pipelines:** Using `venv` + `requirements.txt` guarantees that your automation script runs with the exact same library versions on your laptop, Jenkins runner, and Docker container.

---

## 🧠 Mental model

```mermaid
flowchart TD
    subgraph Host OS Python: /usr/bin/python3
        OS["Linux OS Tools (apt, yum, systemd)"]
    end
    subgraph Project Virtual Environment: ./venv
        Py["Isolated python3 binary"]
        Pip["Isolated pip"]
        Libs["requests==2.31.0<br/>boto3==1.34.0<br/>PyYAML==6.0.1"]
    end
    Host OS Python -.->|Isolated from| Project Virtual Environment
```

---

## 📖 Concept

### 1. The Virtual Environment (`venv`) Workflow
```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate virtual environment
source venv/bin/activate       # Linux / macOS
.\venv\Scripts\Activate.ps1   # Windows PowerShell

# 3. Install packages
pip install requests pyyaml

# 4. Freeze dependencies
pip freeze > requirements.txt

# 5. Install on target server / runner
pip install -r requirements.txt
```

### 2. Modules and Imports
- **Built-in:** `import sys`, `import os`, `import json`, `import time`
- **Third-party:** `import requests`, `import boto3`, `import yaml`
- **Custom local modules:** `from utils import check_disk`

---

## 💻 Simple example

```python
import math
from datetime import datetime

print(f"Current UTC Time: {datetime.utcnow()}")
print(f"Ceil calculation: {math.ceil(4.2)}")  # 5
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Module Inspection & Runtime Environment Audit
"""
import sys
import os
import platform

def audit_python_runtime():
    print("========================================")
    print("     PYTHON RUNTIME ENVIRONMENT AUDIT   ")
    print("========================================")
    
    # 1. Inspecting Python Binary & Version
    python_bin = sys.executable
    version = sys.version.split(" ")[0]
    
    # 2. Detecting if running inside a Virtual Environment
    # In a venv, sys.prefix != sys.base_prefix
    is_in_venv = hasattr(sys, 'real_prefix') or (sys.prefix != getattr(sys, 'base_prefix', sys.prefix))
    
    print(f"Host Node      : {platform.node()}")
    print(f"OS Platform    : {platform.system()} {platform.release()}")
    print(f"Python Executable: {python_bin}")
    print(f"Python Version : {version}")
    print(f"In VirtualEnv  : {is_in_venv}")
    
    if not is_in_venv:
        print("\n[!] WARNING: Running against global/system Python!")
        print("    Recommendation: Create an isolated venv to avoid package contamination.")
    else:
        print("\n[+] SUCCESS: Running inside isolated virtual environment.")
        
    print("========================================")

if __name__ == "__main__":
    audit_python_runtime()
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
     PYTHON RUNTIME ENVIRONMENT AUDIT   
========================================
Host Node      : devops-workstation
OS Platform    : Linux 6.5.0-generic
Python Executable: /home/devops/project/venv/bin/python
Python Version : 3.11.8
In VirtualEnv  : True

[+] SUCCESS: Running inside isolated virtual environment.
========================================
```

---

## 🔍 Line-by-line explanation
- `sys.executable`: Shows the absolute path to the Python binary running this script.
- `sys.prefix != sys.base_prefix`: Standard programmatic way to verify virtual environment isolation.

---

## 🐚 Shell equivalent

```bash
which python3
python3 -c "import sys; print(sys.prefix != sys.base_prefix)"
```

---

## ⚙️ Ansible equivalent

```yaml
- name: Install requirements into isolated virtualenv
  ansible.builtin.pip:
    requirements: /opt/automation/requirements.txt
    virtualenv: /opt/automation/venv
    virtualenv_command: python3 -m venv
```

---

## 🏆 Which one should I use?
- In all production servers and CI runners, always execute Python automation inside a dedicated `venv` or within a single-purpose Docker container.

---

## ⚠️ Common mistakes
1. **Running `sudo pip install package` on Ubuntu 22.04+:**

   - Breaks system Python packages managed by `apt`. Always use `venv`.
2. **Committing `venv/` to Git:**

   - Never commit virtual environments. Add `venv/` and `.venv/` to `.gitignore`.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Create a script that checks if critical DevOps modules (`json`, `sys`, `os`, and optional `yaml` or `requests`) can be imported safely without throwing `ModuleNotFoundError`.

---

## 💡 Hint
Use `try...except ModuleNotFoundError` inside a loop of module names using `__import__(mod_name)`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "What is PEP 668 (`externally-managed-environment`) in modern Linux distributions, and how do you handle it in CI/CD pipelines?"
> **Interviewer Focus:** Testing your familiarity with modern Ubuntu/Debian/RHEL Python packaging standards.

---

## 🗣️ How to answer in an interview
> *"Modern Linux distros mark the system Python environment as 'externally managed' to prevent `pip` from overwriting system packages installed by `apt`/`dnf`, which could break OS utilities. In CI/CD pipelines and server automation, we adhere to best practices by creating a lightweight virtual environment (`python3 -m venv /opt/app/venv`) and installing dependencies there, or by packaging the Python automation script directly inside a minimal container image (like `python:3.11-slim`)."*

---

## 📝 What I should remember
- Never install project packages into `/usr/bin/python3`.
- Always use `python3 -m venv venv`.
- Pin exact versions in `requirements.txt` (`requests==2.31.0`).
- Put `venv/` in your `.gitignore`.
