# Lesson 03 — Numbers and Math in DevOps

## 🎯 What will I learn?
You will learn how to perform calculations in Python: arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`), floating-point rounding (`round()`), calculating disk/memory percentages, converting bytes to gigabytes, and threshold math.

---

## 🤔 Why does a DevOps engineer need this?
DevOps automation revolves around operational metrics:
- Calculating percentage of free disk space from total and used blocks.
- Converting raw bytes from `psutil` or Prometheus into human-readable MB / GB (`bytes / (1024 ** 3)`).
- Rounding CPU averages to 2 decimal places.
- Calculating autoscaling replica requirements: `math.ceil(current_traffic / target_capacity_per_pod)`.

---

## 🧠 Mental model

```mermaid
flowchart LR
    Bytes["Raw Bytes: 53687091200"] -->|"/ (1024 ** 3)"| GB["Gigabytes: 50.0 GB"]
    GB -->|"used / total * 100"| Pct["Usage: 82.4%"]
    Pct -->|"> 80%"| Alert["Trigger Alert"]
```

---

## 📖 Concept

Python handles integers of arbitrary size automatically and supports high-precision floating point numbers.

### DevOps Arithmetic Operators

| Operator | Name | DevOps Example |
| :--- | :--- | :--- |
| `+` | Addition | Total cluster capacity: `node_a + node_b` |
| `-` | Subtraction | Available memory: `total_mem - used_mem` |
| `*` | Multiplication | Estimating monthly cloud cost: `hourly_rate * 730` |
| `/` | Float Division | Disk usage ratio: `used / total` (returns `float`) |
| `//` | Integer (Floor) Division | Max full worker pods: `total_cpu // cpu_per_pod` |
| `%` | Modulo (Remainder) | Round-robin load balancer index: `request_count % num_servers` |
| `**` | Exponentiation | Bytes conversion: `1024 ** 2` (MB), `1024 ** 3` (GB) |

---

## 💻 Simple example

```python
total_mem_bytes = 17179869184  # 16 GB in bytes
used_mem_bytes = 12884901888   # 12 GB in bytes

# Convert to GB
total_gb = total_mem_bytes / (1024 ** 3)
used_gb = used_mem_bytes / (1024 ** 3)

used_percentage = (used_gb / total_gb) * 100
print(f"Used: {round(used_percentage, 2)}%")  # 75.0%
```

---

## 🔧 Real DevOps example (`example.py`)

```python
"""
DevOps Script: Host Disk Capacity Calculator & Cloud Cost Estimator
"""

def audit_disk_and_cost(total_bytes, used_bytes, hourly_instance_cost):
    # 1. Byte conversions using exponents
    bytes_in_gb = 1024 ** 3
    total_gb = total_bytes / bytes_in_gb
    used_gb = used_bytes / bytes_in_gb
    free_gb = total_gb - used_gb
    
    # 2. Percentage calculation with rounding
    used_pct = round((used_gb / total_gb) * 100, 1)
    
    # 3. Cloud monthly cost projection (average month = 730 hours)
    monthly_cost = round(hourly_instance_cost * 730, 2)
    
    print("========================================")
    print("     SYSTEM DISK & COST AUDIT REPORT    ")
    print("========================================")
    print(f"Total Storage : {total_gb:.2f} GB")
    print(f"Used Storage  : {used_gb:.2f} GB ({used_pct}%)")
    print(f"Free Storage  : {free_gb:.2f} GB")
    print(f"Hourly Cost   : ${hourly_instance_cost:.4f}/hr")
    print(f"Monthly Est.  : ${monthly_cost:.2f}/month")
    
    if used_pct >= 85.0:
        print("[!] STATUS: CRITICAL - Disk cleanup required")
    elif used_pct >= 70.0:
        print("[!] STATUS: WARNING - Approaching threshold")
    else:
        print("[+] STATUS: HEALTHY")
    print("========================================")

if __name__ == "__main__":
    # Test with 500GB disk with 430GB used, $0.096/hr instance
    audit_disk_and_cost(
        total_bytes=536870912000,
        used_bytes=461708984320,
        hourly_instance_cost=0.096
    )
```

---

## 🖥️ Expected output

```text
$ python example.py
========================================
     SYSTEM DISK & COST AUDIT REPORT    
========================================
Total Storage : 500.00 GB
Used Storage  : 430.00 GB (86.0%)
Free Storage  : 70.00 GB
Hourly Cost   : $0.0960/hr
Monthly Est.  : $70.08/month
[!] STATUS: CRITICAL - Disk cleanup required
========================================
```

---

## 🔍 Line-by-line explanation
- `1024 ** 3`: Calculates `1024 * 1024 * 1024 = 1,073,741,824` (exact bytes in 1 GiB).
- `round(..., 1)`: Rounds the floating-point result to 1 decimal place.
- `f"{total_gb:.2f}"`: Formatting specifier that displays the float with exactly 2 decimal places.

---

## 🐚 Shell equivalent

```bash
# In Bash, floating point division requires awk or bc:
USED_BYTES=461708984320
TOTAL_BYTES=536870912000
PCT=$(echo "scale=2; ($USED_BYTES / $TOTAL_BYTES) * 100" | bc)
echo "Usage: $PCT%"
```
*Why Python is better:* In Shell, you must pipe strings into `bc` or `awk` for every floating-point operation. If `bc` is missing on a minimal container image (e.g. Alpine/Distroless), the script crashes.

---

## ⚙️ Ansible equivalent

```yaml
- name: Calculate disk usage percentage
  ansible.builtin.set_fact:
    disk_used_pct: "{{ ((ansible_mounts[0].size_total - ansible_mounts[0].size_available) / ansible_mounts[0].size_total * 100) | round(1) }}"
```

---

## 🏆 Which one should I use?
- Use **Python** whenever metrics require floating-point calculations, cost projections, or multiple threshold checks.
- Use **Ansible** when evaluating simple integer limits in playbook conditionals (`when: mem_free_mb < 500`).

---

## ⚠️ Common mistakes
1. **Integer division in Python 2 vs Python 3:**
   - In Python 3, `5 / 2` is `2.5` (float division).
   - `5 // 2` is `2` (floor division).
2. **Floating-point precision surprises:**
   - `0.1 + 0.2` produces `0.30000000000000004` due to IEEE 754 representation. Always use `round()` or formatted strings for display.

---

## 🧪 Practice (Exercise)
Open `exercise.py`. You have a cluster with 3 worker nodes, each having 16 GB of RAM. The services currently consume 38.5 GB. Calculate the total cluster RAM, used percentage, remaining RAM, and how many extra 4 GB pods can safely fit in the remaining memory.

---

## 💡 Hint
Total RAM = `nodes * 16`. Extra pods = `remaining_ram // 4` (use floor division).

---

## ✅ Solution
Check `solution.py` after writing your code.

---

## 🎯 Interview questions

### Q: "How do you calculate resource limits for containers in Python without causing rounding errors?"
> **Interviewer Focus:** Testing your understanding of ceiling vs floor division and metric units (MiB vs MB).

---

## 🗣️ How to answer in an interview
> *"In infrastructure automation, memory is strictly binary (1 GiB = 1024^3 bytes, not 1000^3). When calculating capacity—such as how many pods fit on a node—we use floor division (`//`) or `math.floor()` so we never over-allocate beyond physical limits. For autoscaling up, we use `math.ceil()` so any fractional demand provisions a full new replica."*

---

## 📝 What I should remember
- Use `**` for powers (`1024 ** 3` for GiB).
- Use `/` for exact float division, `//` for integer floor division.
- Use `round(value, n)` or `f"{value:.2f}"` to format decimal numbers cleanly for reports.
