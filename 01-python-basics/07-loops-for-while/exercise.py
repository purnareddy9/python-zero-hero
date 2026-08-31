"""
Lesson 07: Exercise — Fleet Disk Space Auditor

Task:
You are auditing a fleet of web servers.
`fleet_disks = {"web-01": 45, "web-02": 82, "web-03": 30, "web-04": 94, "web-05": 78}`

Requirements:
1. Iterate over the servers using a `for` loop.
2. If disk usage is under 50%, skip it using `continue` (low noise policy).
3. If disk usage is between 50% and 89%, print a `[WARNING]` status for that server.
4. If disk usage reaches 90% or higher, print an immediate `[CRITICAL EMERGENCY]` alert and STOP checking remaining servers using `break`.
"""

fleet_disks = {
    "web-01": 45,
    "web-02": 82,
    "web-03": 30,
    "web-04": 94,
    "web-05": 78
}

# TODO: Implement fleet audit loop using continue and break
