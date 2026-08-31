"""
Lesson 03 (Module 03): Solution — Deployment Replica Status Auditor
"""
import json

cluster_deployments_json = """
{
  "cluster": "prod-useast-1",
  "deployments": [
    {"name": "frontend-web", "desired": 3, "available": 3},
    {"name": "order-service", "desired": 5, "available": 2},
    {"name": "payment-api", "desired": 4, "available": 4},
    {"name": "email-worker", "desired": 2, "available": 0}
  ]
}
"""

def audit_deployments(raw_json):
    data = json.loads(raw_json)
    cluster = data.get("cluster", "unknown")
    deployments = data.get("deployments", [])
    
    degraded = []
    
    for dep in deployments:
        desired = dep.get("desired", 0)
        available = dep.get("available", 0)
        if available < desired:
            degraded.append({
                "name": dep.get("name"),
                "desired": desired,
                "available": available,
                "missing_replicas": desired - available
            })
            
    incident_report = {
        "cluster": cluster,
        "total_deployments": len(deployments),
        "degraded_count": len(degraded),
        "status": "DEGRADED" if degraded else "HEALTHY",
        "incidents": degraded
    }
    
    # Write to incident file
    output_filename = "deployment_incidents.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(incident_report, f, indent=2)
        
    print("========================================")
    print("     DEPLOYMENT REPLICA AUDIT REPORT    ")
    print("========================================")
    print(json.dumps(incident_report, indent=2))
    print("========================================")
    print(f"[+] Incident report saved to '{output_filename}'")

if __name__ == "__main__":
    audit_deployments(cluster_deployments_json)
