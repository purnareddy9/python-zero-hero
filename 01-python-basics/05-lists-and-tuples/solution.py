"""
Lesson 05: Solution — Pod Fleet Sanitizer & Sorter
"""

raw_pods = [
    "auth-canary-78bf",
    "payment-main-99da",
    "auth-main-11ac",
    "checkout-canary-02ef",
    "payment-canary-44bb",
    "checkout-main-33dc"
]

# 1. Filter out non-canary pods
production_pods = []
canary_pods = []

for pod in raw_pods:
    if "canary" in pod:
        canary_pods.append(pod)
    else:
        production_pods.append(pod)

# 2. Sort alphabetically
production_pods.sort()

# 3. Formatted Output
print("========================================")
print("     K8S PRODUCTION FLEET INVENTORY     ")
print("========================================")
print(f"Total Raw Pods     : {len(raw_pods)}")
print(f"Canary Deployments : {len(canary_pods)}")
print(f"Production Stable  : {len(production_pods)}\n")

print("Stable Production Pods:")
for index, pod in enumerate(production_pods, start=1):
    print(f"  {index}. {pod}")
print("========================================")
