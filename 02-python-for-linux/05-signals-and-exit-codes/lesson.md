# Lesson 05 — Signals, Graceful Shutdowns, and Exit Codes in Linux

## 🎯 What will I learn?
You will learn how to handle POSIX operating system signals (`SIGINT`, `SIGTERM`) in Python using the `signal` module, execute graceful cleanup routines before termination, and emit standard Linux exit codes (`sys.exit()`) to integrate cleanly with Docker and Kubernetes pod lifecycles.

---

## 🤔 Why does a DevOps engineer need this?
When Kubernetes terminates a pod or Docker stops a container (`docker stop`), it sends a **`SIGTERM`** signal. The application has a grace period (default 30 seconds) to:

- Finish active HTTP requests or database transactions.
- Close open file handles, sockets, and temporary locks.
- Log an orderly shutdown message.

If your Python script ignores `SIGTERM`, Kubernetes escalates to **`SIGKILL` (`kill -9`)**, forcefully aborting the process and potentially corrupting data.

---

## 🧠 Mental model

```mermaid
flowchart LR
    K8s[Kubernetes Pod Eviction] -->|Sends SIGTERM| Handler[Python signal.signal handler]
    Handler --> Cleanup[Flush buffers, close DB connections, remove PID file]
    Cleanup --> Exit["sys.exit(0) - Orderly Shutdown"]
```

---

## 📖 Concept

### 1. Standard Linux Exit Codes

| Exit Code | Meaning | CI/CD / DevOps Interpretation |
| :--- | :--- | :--- |
| `0` | Success | Step succeeded; proceed to next pipeline stage |
| `1` | General Error | Script failed (e.g. disk threshold breached) |
| `2` | Misuse of Shell Builtins / CLI Syntax | Missing mandatory CLI flags |
| `130` | Terminated by Ctrl+C (`SIGINT`) | Interactive user aborted |
| `143` | Terminated by `SIGTERM` | Kubernetes / Docker stopped the container |

### 2. Capturing Signals with `signal`

```python
import signal
import sys

def handle_shutdown(signum, frame):
    print(f"\n[!] Received signal {signum}. Performing graceful cleanup...")
    # Clean up resources
    sys.exit(0)

# Register handlers for SIGINT (Ctrl+C) and SIGTERM (K8s/Docker stop)
signal.signal(signal.SIGINT, handle_shutdown)
if hasattr(signal, "SIGTERM"):
    signal.signal(signal.SIGTERM, handle_shutdown)
```

---

## 💻 Simple example

```python
import signal
import sys
import time

def on_term(sig, frame):
    print("\n[+] Graceful shutdown complete.")
    sys.exit(0)

signal.signal(signal.SIGINT, on_term)

print("Worker running. Press Ctrl+C to test graceful shutdown...")
# time.sleep(10)
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Resilient Worker Daemon with Graceful SIGTERM/SIGINT Handler
Simulates a long-running queue worker or log consumer.
"""
import signal
import sys
import time
import os

class BackgroundQueueWorker:
    def __init__(self):
        self.is_running = True
        self.processed_items = 0
        self.pid_file = "/tmp/worker.pid"
        
        # Register signal handlers
        signal.signal(signal.SIGINT, self.shutdown_handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, self.shutdown_handler)
            
    def write_pid(self):
        print(f"[*] Worker PID: {os.getpid()}")
        
    def shutdown_handler(self, signum, frame):
        sig_name = "SIGINT (Ctrl+C)" if signum == signal.SIGINT else f"SIGTERM ({signum})"
        print(f"\n[!] Signal received: {sig_name}")
        print("[*] Initiating graceful drain and cleanup sequence...")
        
        self.is_running = False
        # Clean up resources (e.g. flushing buffers, closing sockets)
        print(f"[+] Processed {self.processed_items} items before shutdown.")
        print("[+] Removed PID lock file.")
        print("[+] Orderly shutdown complete. Exiting cleanly (code 0).")
        sys.exit(0)
        
    def run(self, max_iterations=5):
        self.write_pid()
        print("[*] Worker active. Processing queue events...")
        
        for i in range(1, max_iterations + 1):
            if not self.is_running:
                break
            print(f"    -> Processed batch event #{i}")
            self.processed_items += 1
            time.sleep(0.5)
            
        print("[+] Batch processing finished naturally.")

if __name__ == "__main__":
    worker = BackgroundQueueWorker()
    worker.run(max_iterations=4)
```

---

## 🖥️ Expected output

```text
$ python example.py
[*] Worker PID: 18420
[*] Worker active. Processing queue events...
    -> Processed batch event #1
    -> Processed batch event #2
    -> Processed batch event #3
    -> Processed batch event #4
[+] Batch processing finished naturally.
```

---

## 🔍 Line-by-line explanation
- `signal.signal(signal.SIGTERM, self.shutdown_handler)`: Intercepts the termination signal from the OS.
- `if not self.is_running: break`: Loop checks state flag to stop pulling new jobs when shutdown is in progress.
- `sys.exit(0)`: Exits with standard success code so container orchestrators register the exit as clean.

---

## 🐚 Shell equivalent

```bash
# In Bash, trap captures signals:
cleanup() {
    echo "Caught SIGTERM, cleaning up..."
    exit 0
}
trap cleanup SIGINT SIGTERM
```

---

## ⚙️ Ansible equivalent

Ansible manages service signals through the `ansible.builtin.systemd` or `community.docker.docker_container` modules (e.g. configuring `stop_signal: SIGTERM` and `stop_timeout: 30`).

---

## 🏆 Which one should I use?
- In all custom Python daemons, microservices, log processors, and worker containers, **always implement a `signal` handler**.

---

## ⚠️ Common mistakes
1. **Calling `sys.exit(1)` on graceful SIGTERM:**

   - Exiting with `1` causes Kubernetes to report the pod as `Error` or `CrashLoopBackOff` instead of `Completed`. Use `sys.exit(0)` on expected graceful termination.
2. **Performing blocking I/O inside signal handlers:**

   - Keep signal handlers fast to ensure the process exits before the container runtime triggers `SIGKILL`.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. Create a background monitoring worker that registers `signal.SIGINT`. When triggered by Ctrl+C, it prints the total runtime in seconds and safely closes a mock log buffer.

---

## 💡 Hint
Track `start_time = time.time()`. Calculate `time.time() - start_time` in the handler.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "What happens when Kubernetes terminates a pod, and how does your Python application handle it?"
> **Interviewer Focus:** Testing your understanding of pod lifecycle hooks, the difference between SIGTERM and SIGKILL, and data loss prevention.

---

## 🗣️ How to answer in an interview
> *"When a Kubernetes pod is deleted, the Kubelet sends `SIGTERM` to process PID 1 and begins the `terminationGracePeriodSeconds` timer (default 30s). In Python, we catch `SIGTERM` using `signal.signal()`. Our handler stops accepting new connections, drains existing work in flight, closes database pools and temporary files, and exits with code `0`. If the application fails to exit before the grace period expires, Kubelet issues an uncatchable `SIGKILL`, which forcefully terminates the container."*

---

## 📝 What I should remember
- `SIGTERM` is the standard graceful termination signal.
- Catch it using `signal.signal(signal.SIGTERM, handler)`.
- Use `sys.exit(0)` for clean shutdowns, non-zero for failures.
- Never do long, blocking network operations in a signal handler.
