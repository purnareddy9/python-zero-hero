"""
Lesson 01 (Module 02): Exercise — Log File Directory Auditor

Task:
Write a script that accepts a directory path from CLI argument `sys.argv[1]`:
1. If no argument is given, print `"Error: Target directory argument required. Usage: python exercise.py <dir_path>"` and exit with status code 2.
2. If the directory does NOT exist, print `"Error: Directory not found."` and exit with status code 1.
3. Scan the directory:
   - Identify all files ending with `.log`.
   - Calculate their file size in Kilobytes (KB) rounded to 2 decimal places.
4. If no `.log` files are found, print `"No log files detected."`.
5. Print a clean summary table and exit with status code 0.
"""
import sys
import os

# TODO: Implement log file directory scanner using sys.argv and os module
