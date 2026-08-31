"""
Project 05: Solution — Cluster Compliance Grade Calculator
"""
from typing import Tuple

def calculate_compliance_grade(total_resources: int, violations: int) -> Tuple[float, str]:
    if total_resources <= 0:
        return 100.0, "A"
        
    score = round(((total_resources - violations) / total_resources) * 100, 1)
    if score >= 90.0:
        grade = "A"
    elif score >= 80.0:
        grade = "B"
    elif score >= 70.0:
        grade = "C"
    else:
        grade = "F"
        
    return score, grade

if __name__ == "__main__":
    print("=========================================")
    print("      CLUSTER COMPLIANCE SCORE TEST      ")
    print("=========================================")
    test_cases = [(50, 2), (50, 8), (50, 14), (50, 30)]
    for total, viol in test_cases:
        s, g = calculate_compliance_grade(total, viol)
        print(f"Total: {total:>2} | Violations: {viol:>2} -> Score: {s:>5.1f}% | Grade: [{g}]")
    print("=========================================")
