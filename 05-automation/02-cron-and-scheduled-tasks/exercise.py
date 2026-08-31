"""
Lesson 02 (Module 05): Exercise — File Lock Guard

Task:
Write a context manager or function `safe_cron_runner(lock_filepath: str)`:
1. Checks if `lock_filepath` exists. If so, prints `"[ABORT] Lock file exists. Exiting."` and returns `False`.
2. Creates the lock file and writes the current PID (`os.getpid()`).
3. Executes a simulated background task.
4. Guaranteed cleanup: Deletes the lock file in a `finally` block.
5. Returns `True` on successful execution.
"""
import os
import time

# TODO: Implement safe_cron_runner with lock management

if __name__ == "__main__":
    pass
