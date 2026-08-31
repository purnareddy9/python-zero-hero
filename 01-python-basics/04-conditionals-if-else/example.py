"""
Lesson 04: Conditionals (if, elif, else)
Example Script: Microservice Health Evaluator & Traffic Routing Decision
"""

def evaluate_node(node_name, cpu_pct, disk_pct, is_cordoned, active_alerts):
    print(f"[*] Evaluating Node: {node_name}")
    
    # 1. Condition: Is the node explicitly cordoned or under maintenance?
    if is_cordoned:
        status = "MAINTENANCE"
        action = "Do NOT schedule pods. Node is cordoned."
    # 2. Condition: Critical resource exhaustion
    elif cpu_pct >= 90.0 or disk_pct >= 90.0:
        status = "CRITICAL"
        action = f"Drain node immediately! High load (CPU: {cpu_pct}%, Disk: {disk_pct}%)"
    # 3. Condition: Elevated resource warning
    elif cpu_pct >= 75.0 or disk_pct >= 75.0:
        status = "DEGRADED"
        action = "Send warning to Slack channel. Monitor closely."
    # 4. Condition: Healthy and ready
    elif not active_alerts:
        status = "HEALTHY"
        action = "Node is optimal. Ready for workloads."
    else:
        status = "UNKNOWN"
        action = "Investigate unhandled state."
        
    print(f"    Status: [{status}]")
    print(f"    Action: {action}\n")
    return status

if __name__ == "__main__":
    print("========================================")
    print("       K8S NODE HEALTH DECISION         ")
    print("========================================")
    evaluate_node("node-01", cpu_pct=42.0, disk_pct=60.0, is_cordoned=False, active_alerts=[])
    evaluate_node("node-02", cpu_pct=92.5, disk_pct=50.0, is_cordoned=False, active_alerts=[])
    evaluate_node("node-03", cpu_pct=10.0, disk_pct=15.0, is_cordoned=True, active_alerts=[])
    print("========================================")
