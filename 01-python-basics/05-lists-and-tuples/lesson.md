# Lesson 05 — Lists and Tuples in DevOps

## 🎯 What will I learn?
You will learn how to manage ordered collections using **Lists** (`[...]`) and **Tuples** (`(...)`). You will master list operations: appending, removing, slicing, sorting, length checking, and understanding when to use mutable lists versus immutable tuples.

---

## 🤔 Why does a DevOps engineer need this?
DevOps revolves around sequences of infrastructure resources:
- A list of Kubernetes pod names: `["payment-pod-1", "payment-pod-2"]`
- An array of target deployment IP addresses or DNS endpoints.
- A list of ports to scan: `[22, 80, 443, 3306, 8080]`
- An immutable tuple defining fixed database connection coordinates: `("db-prod.internal", 5432)`.

---

## 🧠 Mental model

```mermaid
flowchart LR
    subgraph List: servers (Mutable)
        L0["[0] 'web-01'"]
        L1["[1] 'web-02'"]
        L2["[2] 'web-03'"]
    end
    subgraph Tuple: db_endpoint (Immutable)
        T0["[0] 'db.internal'"]
        T1["[1] 5432"]
    end
```

---

## 📖 Concept

### 1. List (`list`)
- **Mutable:** You can add, remove, and modify elements at any time.
- **Syntax:** `servers = ["web01", "web02"]`
- **Common operations:** `.append()`, `.remove()`, `.pop()`, `len()`, `sorted()`.

### 2. Tuple (`tuple`)
- **Immutable:** Once created, its items and length cannot be changed.
- **Syntax:** `db_config = ("10.0.0.5", 5432)`
- **DevOps use case:** Constants, coordinates, dictionary keys, or function return pairs.

---

## 💻 Simple example

```python
# Working with a server list
servers = ["web-01", "web-02"]
servers.append("web-03")  # Add a server
print(f"Total nodes: {len(servers)}") # 3
print(f"Primary node: {servers[0]}")  # 'web-01'
print(f"Latest node: {servers[-1]}")  # 'web-03'
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Server Pool Management & Port Auditor
"""

# 1. Defining and mutating a cluster worker pool
active_nodes = ["worker-east-01", "worker-east-02", "worker-east-03"]
print(f"[*] Initial Active Node Pool ({len(active_nodes)}): {active_nodes}")

# New node auto-scaled up
active_nodes.append("worker-east-04")
print(f"[+] Scaled up! Node added. Current pool: {active_nodes}")

# A node failed health checks -> remove from load balancer pool
failed_node = "worker-east-02"
if failed_node in active_nodes:
    active_nodes.remove(failed_node)
    print(f"[!] Health check failed for {failed_node}. Removed from active pool.")

# 2. Immutable Configuration Tuples for Service Binding
# Format: (Service Name, Bind Port, Protocol)
STANDARD_PORTS = (
    ("SSH", 22, "TCP"),
    ("HTTP", 80, "TCP"),
    ("HTTPS", 443, "TCP"),
    ("PROMETHEUS", 9090, "TCP")
)

print("\n========================================")
print("     STANDARD PORT SECURITY POLICY      ")
print("========================================")
for service, port, proto in STANDARD_PORTS:
    print(f"Service: {service:<12} | Port: {port:<5} | Protocol: {proto}")
print("========================================")
```

---

## 🖥️ Expected output

```text
$ python example.py
[*] Initial Active Node Pool (3): ['worker-east-01', 'worker-east-02', 'worker-east-03']
[+] Scaled up! Node added. Current pool: ['worker-east-01', 'worker-east-02', 'worker-east-03', 'worker-east-04']
[!] Health check failed for worker-east-02. Removed from active pool.

========================================
     STANDARD PORT SECURITY POLICY      
========================================
Service: SSH          | Port: 22    | Protocol: TCP
Service: HTTP         | Port: 80    | Protocol: TCP
Service: HTTPS        | Port: 443   | Protocol: TCP
Service: PROMETHEUS   | Port: 9090  | Protocol: TCP
========================================
```

---

## 🔍 Line-by-line explanation
- `active_nodes.append(...)`: Adds a new element to the end of the list in $O(1)$ time.
- `if failed_node in active_nodes:`: Safeguards against `ValueError` before calling `.remove()`.
- `for service, port, proto in STANDARD_PORTS:`: **Tuple unpacking** cleanly extracts each item into readable variables.

---

## 🐚 Shell equivalent

```bash
# Bash Arrays
NODES=("worker-01" "worker-02" "worker-03")
NODES+=("worker-04")
echo "Total nodes: ${#NODES[@]}"
echo "First node: ${NODES[0]}"
```
*Why Python is better:* Bash arrays lack native sorting, filtering, and rich data manipulation. Multi-dimensional or mixed-type arrays in Bash are nearly impossible to manage cleanly.

---

## ⚙️ Ansible equivalent

```yaml
- name: Iterate over target ports
  ansible.builtin.debug:
    msg: "Checking port {{ item }}"
  loop:
    - 22
    - 80
    - 443
    - 9090
```

---

## 🏆 Which one should I use?
- Use **Python lists** for dynamic collections that change during script execution (e.g. accumulating unhealthy hosts or failed pods).
- Use **Python tuples** when passing fixed, read-only parameters that should never accidentally be modified.

---

## ⚠️ Common mistakes
1. **IndexError (Out of bounds):**
   ```python
   nodes = ["k8s-01", "k8s-02"]
   # print(nodes[2])  # ❌ IndexError: list index out of range (remember lists are 0-indexed!)
   ```
2. **Attempting to mutate a tuple:**
   ```python
   coords = ("us-east-1", 3)
   # coords[1] = 4    # ❌ TypeError: 'tuple' object does not support item assignment
   ```

---

## 🧪 Practice (Exercise)
Open `exercise.py`. You are given a list of deployed pod names. Filter out any pod that contains `"canary"` in its name, and produce a sorted list of production pods.

---

## 💡 Hint
Create a new empty list `prod_pods = []`, loop over `pods`, and check `if "canary" not in pod: prod_pods.append(pod)`. Then sort using `prod_pods.sort()`.

---

## ✅ Solution
Check `solution.py` after your attempt.

---

## 🎯 Interview questions

### Q: "What is the difference between a list and a tuple in Python, and why would you choose a tuple in an infrastructure tool?"
> **Interviewer Focus:** Testing your memory footprint awareness, immutability concepts, and defensive programming practices.

---

## 🗣️ How to answer in an interview
> *"Lists are mutable (can grow, shrink, and modify items), while tuples are immutable (fixed size and read-only). In DevOps tools, we use tuples for constant configurations—like database coordinates `(host, port)` or fixed HTTP methods `('GET', 'POST', 'DELETE')`—because immutability guarantees that no other part of the script or thread can accidentally mutate critical configuration data during runtime. Tuples also use slightly less memory and can be used as dictionary keys."*

---

## 📝 What I should remember
- Lists use square brackets `[...]` and are mutable.
- Tuples use parentheses `(...)` and are immutable.
- Python is 0-indexed: the first item is `[0]`, the last item is `[-1]`.
- Use `.append()` to add, `.remove()` to delete, and `len()` to get the count.
