"""
Lesson 02 (Module 03): Exercise — Error Rate Calculator

Task:
Write a function `calculate_error_rate(log_filepath: str, max_allowed_error_pct: float = 5.0)`:
1. Streams through `log_filepath` line by line.
2. Counts `total_lines` and `error_lines` (lines containing `"ERROR"` or `"CRITICAL"`).
3. If `total_lines == 0`, return `(True, 0.0)`.
4. Calculates `error_pct = round((error_lines / total_lines) * 100, 2)`.
5. If `error_pct > max_allowed_error_pct`, return `(False, error_pct)`.
6. Otherwise, return `(True, error_pct)`.
"""

# TODO: Implement calculate_error_rate function

if __name__ == "__main__":
    pass
