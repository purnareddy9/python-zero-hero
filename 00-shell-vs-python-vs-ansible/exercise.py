"""
Lesson 00: Exercise — Service Health Validator

Task:
You are given a dictionary of microservices and their HTTP response codes.
Write a script that:
1. Loops through each service and status code.
2. If status code is NOT 200, mark the service as UNHEALTHY and add it to a failure list.
3. If any service is unhealthy, print an alert summary and exit with status code 1.
4. If all services are 200, print "All systems operational" and exit with status code 0.

Hint:
- Use a `for` loop over `services.items()`
- Use `sys.exit(1)` when `failed_services` is not empty.
"""
import sys

services = {
    "auth-service": 200,
    "payment-gateway": 503,
    "user-profile": 200,
    "order-processor": 500
}

def audit_services(service_map):
    # TODO: Write your logic here
    pass

if __name__ == "__main__":
    audit_services(services)
