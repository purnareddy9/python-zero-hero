"""
Lesson 02 (Module 07): Exercise — Deployment Rollout Validator

Task:
Write a function `validate_deployment_health(deployment_dict: dict) -> tuple`:
Given a simulated or real deployment object/dictionary with:
- `spec.replicas`: desired integer
- `status.available_replicas`: running integer
- `status.unavailable_replicas`: missing integer

Requirements:
1. If `available_replicas == desired_replicas` and `unavailable == 0`:
   return `(True, "HEALTHY", 0)`
2. If `available_replicas < desired_replicas`:
   return `(False, "DEGRADED", desired - available)`
3. Handle missing keys defensively using `.get()`.
"""

# TODO: Implement validate_deployment_health function

if __name__ == "__main__":
    pass
