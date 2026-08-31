"""
Lesson 03 (Module 03): Exercise — Deployment Replica Status Auditor

Task:
You receive the following JSON string from a Kubernetes cluster watcher:
`cluster_deployments_json = '''
{
  "cluster": "prod-useast-1",
  "deployments": [
    {"name": "frontend-web", "desired": 3, "available": 3},
    {"name": "order-service", "desired": 5, "available": 2},
    {"name": "payment-api", "desired": 4, "available": 4},
    {"name": "email-worker", "desired": 2, "available": 0}
  ]
}
'''`

Write a script that:
1. Deserializes the JSON string with `json.loads()`.
2. Identifies all deployments where `available < desired`.
3. Constructs an incident summary dictionary.
4. Serializes the incident summary to a file named `deployment_incidents.json` using `json.dump(..., indent=2)`.
5. Prints the formatted JSON to standard output.
"""
import json

# TODO: Implement JSON deployment status audit
