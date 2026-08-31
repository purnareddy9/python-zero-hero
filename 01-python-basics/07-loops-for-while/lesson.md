# Lesson 07 — Loops (for, while, break, continue) in DevOps

## 🎯 What will I learn?
You will learn how to automate repetitive tasks using **`for` loops** and **`while` loops**. You will master `break` (exit early), `continue` (skip to next item), iterating over dictionaries with `.items()`, using `enumerate()` for indexed output, and building resilient polling retry loops with `time.sleep()`.

---

## 🤔 Why does a DevOps engineer need this?
DevOps is the science of repetition:
- Iterating across 50 servers to check disk usage (`for host in servers:`).
- Polling a Kubernetes deployment or AWS RDS instance every 5 seconds until status is `"AVAILABLE"` (`while status != "AVAILABLE":`).
- Retrying an API call up to 3 times before giving up (`for attempt in range(3):`).
- Skipping comments or blank lines when reading configuration files (`if line.startswith("#"): continue`).

---

## 🧠 Mental model

```mermaid
flowchart TD
    subgraph For Loop: Batch Iteration
        FStart([Start for host in hosts]) --> FAction[Check host health]
        FAction --> FNext{More hosts?}
        FNext -->|Yes| FAction
        FNext -->|No| FEnd([Finished Batch])
    end
    subgraph While Loop: Polling / Retry
        WStart([Start while attempts < 5]) --> WCheck{Service Ready?}
        WCheck -->|Yes| WSuccess([break - Ready!])
        WCheck -->|No| WWait[time.sleep(2) -> attempts += 1]
        WWait --> WCheck
    end
```

---

## 📖 Concept

### 1. `for` Loop
Used when you have a known collection or range of items (servers, lines, pods, numbers).
```python
for item in collection:
    # do action
```

### 2. `while` Loop
Used when you need to repeat an action until a specific condition becomes true/false (polling a server or deployment).
```python
while condition:
    # keep doing until condition changes
```

### 3. Control Statements
- `break`: Terminate the loop immediately.
- `continue`: Skip the rest of the current iteration and move directly to the next.

---

## 💻 Simple example

```python
# Skipping comments with continue
config_lines = ["# Database Configuration", "HOST=10.0.0.1", "# Port setting", "PORT=5432"]

for line in config_lines:
    if line.startswith("#"):
        continue  # Skip comments
    print(f"Applying setting: {line}")
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Deployment Readiness Polling & Server Fleet Health Checker
"""
import time

def simulate_service_polling(max_retries=4, delay_seconds=1):
    print("========================================")
    print("   DEPLOYMENT STATUS POLLING SERVICE    ")
    print("========================================")
    
    # Simulate service transitioning from PENDING -> INITIALIZING -> READY
    mock_status_sequence = ["PENDING", "PENDING", "INITIALIZING", "READY"]
    
    attempt = 1
    is_ready = False
    
    while attempt <= max_retries:
        current_status = mock_status_sequence[attempt - 1]
        print(f"[*] [Attempt {attempt}/{max_retries}] Checking service readiness... Status: {current_status}")
        
        if current_status == "READY":
            print("[+] Service is READY! Traffic routing enabled.")
            is_ready = True
            break
            
        print(f"    Waiting {delay_seconds}s before next probe...")
        time.sleep(delay_seconds)
        attempt += 1
        
    if not is_ready:
        print("[!] TIMEOUT ERROR: Service failed to reach READY state within threshold.")
        return False
        
    print("========================================")
    return True

if __name__ == "__main__":
    simulate_service_polling()
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
   DEPLOYMENT STATUS POLLING SERVICE    
========================================
[*] [Attempt 1/4] Checking service readiness... Status: PENDING
    Waiting 1s before next probe...
[*] [Attempt 2/4] Checking service readiness... Status: PENDING
    Waiting 1s before next probe...
[*] [Attempt 3/4] Checking service readiness... Status: INITIALIZING
    Waiting 1s before next probe...
[*] [Attempt 4/4] Checking service readiness... Status: READY
[+] Service is READY! Traffic routing enabled.
========================================
```

---

## 🔍 Line-by-line explanation
- `while attempt <= max_retries:`: Guarantees that the polling loop cannot run indefinitely into an infinite freeze.
- `if current_status == "READY": break`: Exits the while loop immediately upon success.
- `time.sleep(delay_seconds)`: Pauses execution for $N$ seconds between health probes.

---

## 🐚 Shell equivalent

```bash
ATTEMPTS=0
MAX=4
while [ $ATTEMPTS -lt $MAX ]; do
    STATUS=$(curl -s http://localhost:8080/health)
    if [ "$STATUS" = "READY" ]; then
        echo "Service is ready"
        exit 0
    fi
    sleep 1
    ATTEMPTS=$((ATTEMPTS + 1))
done
echo "Timeout"
exit 1
```

---

## ⚙️ Ansible equivalent

```yaml
- name: Wait for service port to become open
  ansible.builtin.wait_for:
    port: 8080
    delay: 2
    timeout: 30
```

---

## 🏆 Which one should I use?
- Use **Python `while` loops** when building custom health checkers with dynamic exponential backoff, JSON payload inspection, or multi-stage readiness verification.
- Use **Ansible `wait_for`** for standard port or file readiness checks in infrastructure setup playbooks.

---

## ⚠️ Common mistakes
1. **Accidental infinite loops:**
   ```python
   # while is_pending:   # If is_pending is never updated inside the loop, the CPU will max out!
   ```
   *Fix:* Always use a `max_attempts` counter or a timeout limit.
2. **Modifying a list while iterating over it:**
   ```python
   # for item in items: items.remove(item)  # ❌ Skipping elements bug!
   # Instead, iterate over a copy or use list comprehension:
   items = [x for x in items if keep(x)]    # ✅ Safe
   ```

---

## 🧪 Practice (Exercise)
Open `exercise.py`. You have a fleet of 5 servers with disk utilization numbers. Write a loop that prints the status of each server. If disk usage > 90%, print a CRITICAL alert and stop checking further servers immediately (`break`). If disk usage is below 50%, skip detailed metrics (`continue`).

---

## 💡 Hint
Use `for server, disk in fleet.items():` and compare `disk > 90` with `break`, and `disk < 50` with `continue`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "How would you write a resilient polling retry loop in Python to check an external API?"
> **Interviewer Focus:** Testing your understanding of timeouts, exponential backoff, maximum retry limits, and avoiding tight CPU loops.

---

## 🗣️ How to answer in an interview
> *"A production-grade retry loop in Python should never loop infinitely. I implement a `for attempt in range(1, max_retries + 1)` loop, paired with a timeout on the network call. Between failed attempts, I implement exponential backoff (`delay = base_delay * (2 ** attempt)`) plus a slight jitter to prevent the 'thundering herd' problem against the backend service. If `max_retries` is exceeded, I raise a custom exception or exit with a non-zero code for the orchestrator."*

---

## 📝 What I should remember
- Use `for` loops for bounded collections (`for pod in pods:`).
- Use `while` loops for state polling, always bounded by a `max_attempts` counter.
- Use `break` to exit early on success or critical error.
- Use `continue` to skip non-actionable items (like comments or healthy hosts).
