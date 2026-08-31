# Lesson 03 — Production Logging vs `print()` in DevOps

## 🎯 What will I learn?
You will learn why `print()` is unsuitable for production automation and master Python's built-in `logging` module: understanding log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`), configuring formatters with timestamps and process IDs, outputting to both console and rotating log files, and integrating with centralized log forwarders (Fluentd, Promtail/Loki, Datadog).

---

## 🤔 Why does a DevOps engineer need this?
In production systems:
- `print()` messages lack severity levels, timestamps, and line numbers, making post-incident debugging impossible.
- Log aggregation systems (Elasticsearch, CloudWatch, Grafana Loki) parse structured formats (JSON / standard syslog).
- Setting log level to `INFO` in production hides noisy debug traces, but changing to `DEBUG` dynamically during an outage reveals detailed HTTP payload traces without touching code.

---

## 🧠 Mental model

```mermaid
flowchart TD
    Script["Python Automation Code"] --> Log["logging.getLogger('DeployEngine')"]
    Log --> LevelCheck{"Log Level >= INFO?"}
    LevelCheck -->|DEBUG (Dropped)| Discard[Discard]
    LevelCheck -->|INFO / WARN / ERROR| Formatter["Formatter: [2026-08-31 14:18] [ERROR] [PID:123]"]
    Formatter --> StreamHandler["StreamHandler (Console / stdout)"]
    Formatter --> FileHandler["RotatingFileHandler (/var/log/deploy.log)"]
```

---

## 📖 Concept

### The 5 Standard Python Log Levels

| Level | Value | DevOps Use Case |
| :--- | :--- | :--- |
| `DEBUG` | 10 | Verbose HTTP payloads, SQL queries, raw command tokens |
| `INFO` | 20 | Normal operational events: "Deployment started", "Server added" |
| `WARNING`| 30 | Elevated metrics, deprecated API calls, retry attempts |
| `ERROR` | 40 | Non-fatal failures: "Node unreachable", "API timeout on attempt 2" |
| `CRITICAL`| 50 | Fatal crashes: "Database pool exhausted", "All 3 zones down" |

---

## 💻 Simple example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Starting cluster scan...")
logging.warning("Node 04 is approaching memory limit")
logging.error("Failed to connect to Redis cache")
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Enterprise Multi-Handler Rotating Logging System
Emits formatted logs to stdout and rotating log files simultaneously.
"""
import logging
from logging.handlers import RotatingFileHandler
import os

def setup_production_logger(logger_name="devops-engine", log_file="automation.log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Capture all levels
    
    # Prevent duplicate handlers if called multiple times
    if logger.handlers:
        return logger
        
    # Standard format: Timestamp, Log Level, Component, Message
    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(name)s] [PID:%(process)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # 1. Console Handler (stdout) - shows INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    # 2. Rotating File Handler (max 1 MB per file, keeps 3 backups) - saves DEBUG and above
    file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    
    return logger

def run_backup_pipeline():
    logger = setup_production_logger()
    
    logger.info("Starting automated database snapshot pipeline...")
    logger.debug("Connecting to target RDS instance at endpoint: rds-primary.internal:5432")
    
    # Simulate operation
    db_storage_used_pct = 82.5
    if db_storage_used_pct > 80.0:
        logger.warning(f"Database storage threshold warning: {db_storage_used_pct}% utilized.")
        
    # Simulate minor error
    logger.error("Snapshot replica synchronization experienced 1 retry attempt.")
    
    logger.info("Snapshot pipeline execution concluded.")

if __name__ == "__main__":
    run_backup_pipeline()
```

---

## 🖥️ Expected output

```text
$ python example.py
2026-08-31 14:18:22 [INFO] [devops-engine] [PID:19420] Starting automated database snapshot pipeline...
2026-08-31 14:18:22 [WARNING] [devops-engine] [PID:19420] Database storage threshold warning: 82.5% utilized.
2026-08-31 14:18:22 [ERROR] [devops-engine] [PID:19420] Snapshot replica synchronization experienced 1 retry attempt.
2026-08-31 14:18:22 [INFO] [devops-engine] [PID:19420] Snapshot pipeline execution concluded.
```

---

## 🔍 Line-by-line explanation
- `RotatingFileHandler(..., maxBytes=1_000_000, backupCount=3)`: Protects the server disk from filling up by automatically rotating logs when they reach 1 MB, keeping at most 3 historical files (`automation.log.1`, etc.).
- `%(asctime)s [%(levelname)s] [PID:%(process)d]`: Standard syslog-compliant format.
- `logger.setLevel(logging.DEBUG)`: Allows debug messages to be captured in the file while console output only displays `INFO` and above.

---

## 🐚 Shell equivalent

```bash
# In Bash, redirecting output:
echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] Pipeline started" | tee -a automation.log
```

---

## ⚙️ Ansible equivalent

Ansible controls log output via `ANSIBLE_LOG_PATH=/var/log/ansible.log` and the `ansible.builtin.debug` module with `verbosity: 1`.

---

## 🏆 Which one should I use?
- In all production Python scripts, **always use the `logging` module** instead of `print()`.

---

## ⚠️ Common mistakes
1. **Using `print()` for errors:**
   - `print()` writes to `stdout` instead of `stderr` and lacks timestamps, causing log ingestors to misclassify errors.
2. **Missing `logger.handlers` check:**
   - In modular scripts or webhooks, configuring loggers repeatedly will attach duplicate handlers, causing every message to print 2 or 3 times.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Create a function `get_configured_logger(name, is_debug_mode=False)` that sets the console log level to `DEBUG` if `is_debug_mode` is True, otherwise `INFO`.

---

## 💡 Hint
Call `console_handler.setLevel(logging.DEBUG if is_debug_mode else logging.INFO)`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "Why is `print()` an anti-pattern in production DevOps automation, and how does the `logging` module solve it?"
> **Interviewer Focus:** Testing your understanding of log levels, standard output vs standard error, and observability integration.

---

## 🗣️ How to answer in an interview
> *"`print()` is an anti-pattern because it provides no severity levels, no timestamps, cannot be filtered dynamically at runtime, and dumps everything directly to standard output. The Python `logging` module provides granular log levels (`DEBUG` through `CRITICAL`), structured formatting with timestamps and process IDs, multiple handler destinations (writing to stdout for Kubernetes container log scrapers and rotating files for VMs), and the ability to toggle verbose debug logging via environment variables without modifying source code."*

---

## 📝 What I should remember
- Never use `print()` in production scripts.
- Use `logging.getLogger(__name__)`.
- Configure `RotatingFileHandler` to prevent disk exhaustion.
- Use log levels: `DEBUG` (troubleshooting), `INFO` (audit), `WARNING` (degraded), `ERROR` (failures).
