"""
Lesson 01 (Module 05): Exercise — Disk Audit CLI Tool

Task:
Build a command-line utility with `argparse` that accepts:
1. `-m`, `--mount`: Mandatory string argument for mount path (e.g. `/`, `/var`, `C:\\`).
2. `-t`, `--threshold`: Optional integer argument for disk percentage threshold (default: 85).
3. `--notify`: Optional boolean flag (switch) to simulate sending an alert.

When executed:
- Print the configuration values.
- If threshold >= 90, print `[CRITICAL WARNING] High threshold configured!`.
- If `--notify` is passed, print `[ALERT] Notification dispatched to on-call channel.`.
"""
import argparse

# TODO: Implement the disk audit CLI utility with argparse

if __name__ == "__main__":
    pass
