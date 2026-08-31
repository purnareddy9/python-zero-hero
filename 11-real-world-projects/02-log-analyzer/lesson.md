# Project 02 — Production Application Log Analyzer & Error Aggregator

## 🎯 What will I learn?
You will build a full-featured, streaming log analysis utility in Python that extracts HTTP status codes, counts error rates, groups stack traces, and outputs a formatted terminal incident report.

---

## 🧠 Mental model

```mermaid
flowchart LR
    LogFile["production.log (10 GB)"] --> Stream["Streaming Line Reader"]
    Stream --> Regex["Regex Parser: Level, IP, Route, Status"]
    Regex --> Aggregator["Counter & Incident Map"]
    Aggregator --> Output["Summary Report + Top 5 Outage Causes"]
```

---

## 🔧 Production Implementation (`example.py`)

```python
"""
Project 02: Production Application Log Analyzer & Error Aggregator
Processes logs line-by-line, aggregates statistics, and detects error spikes.
"""
from collections import Counter
import re
import os

LOG_LINE_REGEX = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[(?P<level>[A-Z]+)\]\s+(?P<message>.*)$'
)

def analyze_application_log(filepath):
    print("=========================================")
    print("     PRODUCTION LOG ANALYZER REPORT      ")
    print("=========================================")
    print(f"File Target: {os.path.abspath(filepath)}\n")
    
    if not os.path.exists(filepath):
        print(f"[!] Log file '{filepath}' not found.")
        return
        
    total_lines = 0
    level_counts = Counter()
    error_reasons = Counter()
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            match = LOG_LINE_REGEX.match(line.strip())
            if match:
                lvl = match.group("level")
                msg = match.group("message")
                level_counts[lvl] += 1
                if lvl in ["ERROR", "CRITICAL"]:
                    # Isolate error message category
                    error_tag = msg.split(":")[0] if ":" in msg else msg[:40]
                    error_reasons[error_tag] += 1
                    
    error_total = level_counts["ERROR"] + level_counts["CRITICAL"]
    error_rate = round((error_total / total_lines) * 100, 2) if total_lines > 0 else 0.0
    
    print(f"Total Lines Processed : {total_lines}")
    print(f"Overall Error Rate    : {error_rate}%\n")
    
    print("Log Level Distribution:")
    for lvl, count in sorted(level_counts.items(), key=lambda x: x[1], reverse=True):
        pct = round((count / total_lines) * 100, 1)
        print(f"  - {lvl:<8} : {count:>5} ({pct:>4}%)")
        
    print("\nTop 3 Root Causes:")
    for reason, count in error_reasons.most_common(3):
        print(f"  [!] {reason:<35} : {count} occurrences")
        
    print("=========================================")

if __name__ == "__main__":
    demo_file = "app_prod.log"
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write("2026-08-31 10:01:00 [INFO] Application worker initialized\n")
        f.write("2026-08-31 10:01:05 [INFO] Request GET /api/v1/health 200\n")
        f.write("2026-08-31 10:01:10 [WARN] High memory consumption detected\n")
        f.write("2026-08-31 10:01:15 [ERROR] DatabaseConnectionError: Connection pool exhausted\n")
        f.write("2026-08-31 10:01:20 [ERROR] DatabaseConnectionError: Connection pool exhausted\n")
        f.write("2026-08-31 10:01:25 [CRITICAL] RedisTimeoutError: Failed to reach cache node\n")
        
    analyze_application_log(demo_file)
```

---

## 🖥️ Expected output

```text
$ python example.py
=========================================
     PRODUCTION LOG ANALYZER REPORT      
=========================================
File Target: /home/devops/app_prod.log

Total Lines Processed : 6
Overall Error Rate    : 50.0%

Log Level Distribution:
  - ERROR    :     2 (33.3%)
  - INFO     :     2 (33.3%)
  - CRITICAL :     1 (16.7%)
  - WARN     :     1 (16.7%)

Top 3 Root Causes:
  [!] DatabaseConnectionError             : 2 occurrences
  [!] RedisTimeoutError                   : 1 occurrences
=========================================
```

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Enhance the parser to extract and report unique client IP addresses associated with error lines.

---

## ✅ Solution
Check `solution.py` after your attempt.
