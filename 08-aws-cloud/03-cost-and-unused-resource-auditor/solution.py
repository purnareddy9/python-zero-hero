"""
Lesson 03 (Module 08): Solution — FinOps EBS Waste Calculator
"""
from typing import List, Dict, Any, Tuple

def calculate_ebs_monthly_waste(volumes: List[Dict[str, Any]], rate_per_gb: float = 0.08) -> Tuple[int, int, float]:
    orphans = [v for v in volumes if v.get("State") == "available"]
    total_gb = sum(v.get("Size", 0) for v in orphans)
    total_cost = round(total_gb * rate_per_gb, 2)
    return len(orphans), total_gb, total_cost

if __name__ == "__main__":
    mock_fleet = [
        {"VolumeId": "vol-111", "Size": 100, "State": "in-use"},
        {"VolumeId": "vol-222", "Size": 200, "State": "available"},
        {"VolumeId": "vol-333", "Size": 500, "State": "available"},
        {"VolumeId": "vol-444", "Size": 50, "State": "in-use"}
    ]
    
    print("========================================")
    print("      EBS STORAGE FINOPS CALCULATION    ")
    print("========================================")
    count, gb, cost = calculate_ebs_monthly_waste(mock_fleet)
    print(f"Orphan Volumes Count : {count}")
    print(f"Total Unattached Size: {gb} GB")
    print(f"Monthly Waste Cost   : ${cost:.2f} / month")
    print("========================================")
