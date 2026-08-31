"""
Lesson 03 (Module 08): Exercise — FinOps EBS Waste Calculator

Task:
Write a function `calculate_ebs_monthly_waste(volumes: list, rate_per_gb: float = 0.08) -> tuple`:
Given a list of volume dictionaries with keys `{"VolumeId": str, "Size": int, "State": str}`:
1. Filter only volumes where `State == "available"`.
2. Compute `total_wasted_gb`.
3. Compute `total_wasted_cost = round(total_wasted_gb * rate_per_gb, 2)`.
4. Return `(len(orphan_volumes), total_wasted_gb, total_wasted_cost)`.
"""

# TODO: Implement calculate_ebs_monthly_waste function

if __name__ == "__main__":
    pass
