"""
Lesson 04 (Module 04): Exercise — Database Readiness Probe

Task:
Write a function `wait_for_service_port(host: str, port: int, timeout_sec: int = 5, probe_interval_sec: float = 1.0) -> bool`:
1. Loops until `elapsed_time >= timeout_sec`.
2. Tests if `(host, port)` is accepting TCP connections using `socket.socket()`.
3. If port is open (`connect_ex == 0`), print success message and return `True`.
4. If closed, sleep for `probe_interval_sec` and retry.
5. If timeout expires, return `False`.
"""
import socket
import time

# TODO: Implement wait_for_service_port function

if __name__ == "__main__":
    pass
