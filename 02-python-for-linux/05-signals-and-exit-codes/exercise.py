"""
Lesson 05 (Module 02): Exercise — Graceful Metrics Aggregator

Task:
Build a metrics collector loop that:
1. Records start timestamp with `time.time()`.
2. Registers a signal handler for `signal.SIGINT`.
3. Runs a continuous loop simulating metrics collection (`time.sleep(1)`).
4. When `SIGINT` is received:
   - Calculate total runtime: `elapsed = round(time.time() - start_time, 2)`
   - Print `"Gracefully flushed metrics buffer. Total runtime: X seconds."`
   - Exit with status code 0.
"""
import signal
import sys
import time

# TODO: Implement graceful metrics collector with signal handler

if __name__ == "__main__":
    pass
