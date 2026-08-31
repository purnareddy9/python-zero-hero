"""
Lesson 08: Exercise — CPU Load Normalizer & Alert Function

Task:
Write a reusable function `evaluate_cpu_load(hostname: str, load_avg_15m: float, core_count: int = 4)`:
1. Calculates `normalized_load = load_avg_15m / core_count`.
2. Returns a dictionary with keys:
   - `"hostname"`: str
   - `"normalized_load"`: float (rounded to 2 decimal places)
   - `"is_overloaded"`: bool (True if normalized_load >= 1.0, otherwise False)
   - `"status"`: str ("CRITICAL" if >= 1.0, "ELEVATED" if >= 0.7, "NORMAL" otherwise)
"""

# TODO: Implement evaluate_cpu_load function

if __name__ == "__main__":
    # Test cases:
    # Host 1: 4 cores, load 2.5 -> normalized = 0.62 (NORMAL)
    # Host 2: 4 cores, load 5.2 -> normalized = 1.30 (CRITICAL)
    # Host 3: 8 cores, load 6.0 -> normalized = 0.75 (ELEVATED)
    pass
