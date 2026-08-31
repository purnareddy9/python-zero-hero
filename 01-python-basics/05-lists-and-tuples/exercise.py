"""
Lesson 05: Exercise — Pod Fleet Sanitizer & Sorter

Task:
You query Kubernetes and receive a raw list of running pods.
`raw_pods = ["auth-canary-78bf", "payment-main-99da", "auth-main-11ac", "checkout-canary-02ef", "payment-canary-44bb", "checkout-main-33dc"]`

Requirements:
1. Filter out all canary pods (any pod containing the substring `"canary"`).
2. Store the remaining production pods in a new list `production_pods`.
3. Sort `production_pods` alphabetically.
4. Print the total count of filtered production pods and list them with their 1-based index (e.g. `1. auth-main-11ac`).
"""

raw_pods = [
    "auth-canary-78bf",
    "payment-main-99da",
    "auth-main-11ac",
    "checkout-canary-02ef",
    "payment-canary-44bb",
    "checkout-main-33dc"
]

# TODO: Implement pod filtering and sorting logic here
