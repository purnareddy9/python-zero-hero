# Lesson 02 — Parsing Large Log Files Without Crashing Memory

## 🎯 What will I learn?
You will learn how to stream and analyze multi-gigabyte production log files in Python using **iterators** and **generators** with constant memory usage ($O(1)$ memory). You will learn how to count log levels (`INFO`, `WARN`, `ERROR`), extract top HTTP 500 error causes, and calculate error rates.

---

## 🤔 Why does a DevOps engineer need this?
In production, log files from Nginx, Apache, or Kubernetes pods can reach 10 GB to 50 GB.

- If you run `f.read()` or `f.readlines()`, Python attempts to load the entire 10 GB file into RAM at once, triggering the **Linux OOM (Out-Of-Memory) Killer** to instantly kill your script.
- Iterating line-by-line (`for line in f:`) streams only 1 line into RAM at a time, allowing you to parse a 50 GB log file using less than **20 MB of RAM**!

---

## 🧠 Mental model

```mermaid
flowchart TD
    subgraph Memory Exhaustion Trap: f.readlines
        File10GB["10 GB Log File on Disk"] -->|"Load ALL into RAM"| RAM_Crash["💥 RAM Exhaustion (OOM Killed)"]
    end
    subgraph DevOps Best Practice: Streaming Iterator
        File10GB_Stream["10 GB Log File on Disk"] -->|"1 line at a time"| Buffer["Buffer (2 KB in RAM)"]
        Buffer --> Process["Extract & Update Counter"]
        Process --> NextLine["Discard & Stream Next Line"]
    end
```

---

## 📖 Concept

### Iterating Line-by-Line (Constant Memory)

```python
# ✅ PRODUCTION SAFE: Streams 1 line at a time (O(1) memory)
with open("huge_production.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            # Process line
            pass
```

### Contrast with Dangerous Patterns:
```python
# ❌ NEVER DO THIS ON LARGE FILES:
# data = f.read()        # Loads entire file as a single giant string
# lines = f.readlines()  # Loads all lines into a giant list in memory
```

---

## 💻 Simple example

```python
# Counting errors in a stream
error_count = 0
with open("sample.log", "w", encoding="utf-8") as f:
    f.write("INFO App up\nERROR DB timeout\nINFO Request ok\nERROR Redis down\n")

with open("sample.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

print(f"Total Errors Found: {error_count}") # 2
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: High-Performance Streaming Log Analyzer
Processes logs line-by-line, aggregates HTTP error codes and log levels.
"""
from collections import Counter
import os

def generate_mock_log(filename="production_access.log", count=1000):
    """Generates sample access log entries for demonstration."""
    sample_templates = [
        "2026-08-31 10:01:02 [INFO] GET /api/v1/users 200 12ms",
        "2026-08-31 10:01:05 [INFO] POST /api/v1/checkout 201 45ms",
        "2026-08-31 10:01:10 [WARN] GET /api/v1/products 404 8ms",
        "2026-08-31 10:01:14 [ERROR] POST /api/v1/payment 500 DB_CONNECTION_TIMEOUT",
        "2026-08-31 10:01:18 [ERROR] GET /api/v1/orders 503 SERVICE_UNAVAILABLE",
        "2026-08-31 10:01:22 [ERROR] POST /api/v1/payment 500 DB_CONNECTION_TIMEOUT"
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(count):
            f.write(sample_templates[i % len(sample_templates)] + "\n")

def stream_analyze_log(filepath):
    print("========================================")
    print("      STREAMING LOG FILE ANALYZER       ")
    print("========================================")
    print(f"Analyzing: {os.path.abspath(filepath)}")
    
    total_lines = 0
    level_counts = Counter()
    error_reasons = Counter()
    
    # Stream line by line (O(1) memory consumption)
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            line = line.strip()
            
            # Extract log level
            if "[INFO]" in line:
                level_counts["INFO"] += 1
            elif "[WARN]" in line:
                level_counts["WARN"] += 1
            elif "[ERROR]" in line:
                level_counts["ERROR"] += 1
                # Extract error reason if present
                parts = line.split(" ")
                if len(parts) >= 6:
                    error_reasons[parts[-1]] += 1
                    
    print(f"Total Lines Processed : {total_lines}")
    print("----------------------------------------")
    print("Log Level Breakdown:")
    for level, count in level_counts.items():
        pct = round((count / total_lines) * 100, 2)
        print(f"  - {level:<6} : {count:>5} ({pct}%)")
        
    print("----------------------------------------")
    print("Top Error Root Causes:")
    for reason, count in error_reasons.most_common(3):
        print(f"  - {reason:<25} : {count} occurrences")
        
    print("========================================")

if __name__ == "__main__":
    log_file = "production_access.log"
    generate_mock_log(log_file, count=600)
    stream_analyze_log(log_file)
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
      STREAMING LOG FILE ANALYZER       
========================================
Analyzing: /home/devops/production_access.log
Total Lines Processed : 600
----------------------------------------
Log Level Breakdown:

  - INFO   :   200 (33.33%)
  - WARN   :   100 (16.67%)
  - ERROR  :   300 (50.0%)
----------------------------------------
Top Error Root Causes:

  - DB_CONNECTION_TIMEOUT     : 200 occurrences
  - SERVICE_UNAVAILABLE       : 100 occurrences
========================================
```

---

## 🔍 Line-by-line explanation
- `from collections import Counter`: High-performance dictionary subclass designed specifically for counting frequency of occurrences.
- `with open(...) as f: for line in f:`: Python's file iterator streams data from disk buffers in small chunks without loading the whole file into RAM.
- `error_reasons.most_common(3)`: Efficiently retrieves the top 3 most frequent error messages.

---

## 🐚 Shell equivalent

```bash
# In Bash:
awk '{print $3}' production_access.log | sort | uniq -c
```
*Why Python is better:* In Shell, `sort` on a 10 GB file will create massive temporary files in `/tmp` and consume high CPU/disk I/O. Python streaming evaluates everything in a single linear $O(N)$ pass.

---

## ⚙️ Ansible equivalent

Ansible is not designed for log analysis or streaming gigabyte files.

---

## 🏆 Which one should I use?
- Use **Python streaming iterators** whenever you need to build custom log parsers, aggregate error rates, or extract telemetry without risking host OOM crashes.

---

## ⚠️ Common mistakes
1. **Using `f.readlines()` on unknown file sizes:**

   - Always assume production logs can be huge. Always use `for line in f:`.
2. **Accumulating all lines in a `list`:**

   - If you do `all_errors.append(line)` for 10 million lines, you re-introduce the exact memory leak you were trying to avoid! Store only aggregated counts or metrics.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Write a streaming log parser that scans a log file line by line and computes the **Error Rate Percentage**: `(total_error_lines / total_lines) * 100`. If Error Rate > 5.0%, return `(False, error_rate)`.

---

## 💡 Hint
Keep two integer counters: `total_lines` and `error_lines`. Increment appropriately inside `for line in f:`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "How would you process a 20 GB log file in Python on a server that only has 1 GB of available RAM?"
> **Interviewer Focus:** Testing your understanding of file stream iterators, generator functions, and garbage collection.

---

## 🗣️ How to answer in an interview
> *"I use Python's built-in file iterator with a context manager (`with open(...) as f: for line in f:`). Instead of calling `read()` or `readlines()`, which would crash the system with an Out-of-Memory error, the file iterator reads only one line into memory at a time. I process each line in-flight, update running counters or write matches to an output stream, allowing the garbage collector to immediately reclaim memory. This enables us to process a 20 GB file with less than 25 MB of resident memory."*

---

## 📝 What I should remember
- `for line in f:` streams lines one by one.
- Never use `f.read()` or `f.readlines()` on production logs.
- Use `collections.Counter` for fast frequency counting.
- Keep in-memory state minimal (counts and stats, not full lines).
