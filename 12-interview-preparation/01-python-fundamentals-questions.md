# Interview Module 01 — Python Fundamentals Question Bank

## Q1: How does memory management and garbage collection work in Python?
### 🗣️ Natural Senior DevOps Answer:
> *"Python uses a dual memory management model: **Reference Counting** as its primary mechanism and a **Generational Garbage Collector** to detect and clear circular references. Every object tracks how many references point to it; when reference count drops to zero, the memory is immediately deallocated. In DevOps log streaming or large data batch jobs, being mindful of object references ensures we don't accumulate large lists in global scope that prevent memory reclamation."*

---

## Q2: What is the difference between mutable and immutable types in Python?
### 🗣️ Natural Senior DevOps Answer:
> *"Immutable types—like strings, integers, floats, and tuples—cannot be altered after creation; modifying them creates a new object in memory. Mutable types—like lists, dictionaries, and sets—can be modified in place. In DevOps scripting, passing mutable objects like dictionaries into worker threads or functions can cause race conditions or state mutation bugs if not copied defensively."*

---

## Q3: What is the difference between shallow copy and deep copy?
### 🗣️ Natural Senior DevOps Answer:
> *"A shallow copy (`copy.copy()` or `dict.copy()`) creates a new container object but inserts references to the original nested child objects. A deep copy (`copy.deepcopy()`) recursively copies both the container and all nested objects. When modifying nested infrastructure configurations (like Kubernetes JSON specs or multi-region deployment maps), deep copy ensures that altering the staging dictionary does not unintentionally mutate the production baseline."*

---

## Q4: Why should you avoid mutable default arguments in Python functions?
### 🗣️ Natural Senior DevOps Answer:
> *"In Python, default arguments are evaluated only once when the function is defined, not on every call. If you write `def deploy_host(host, host_list=[])`, subsequent calls share the exact same list in memory. Best practice is `def deploy_host(host, host_list=None): if host_list is None: host_list = []`."*

---

## Q5: What are list comprehensions and generator expressions, and when would you use a generator?
### 🗣️ Natural Senior DevOps Answer:
> *"A list comprehension (`[x for x in items if cond]`) builds and returns the entire list in memory immediately. A generator expression (`(x for x in items if cond)`) returns a lazy iterator that produces one item on demand. When processing a 10 GB access log, a list comprehension will exhaust host RAM, whereas a generator streams items with $O(1)$ constant memory."*
