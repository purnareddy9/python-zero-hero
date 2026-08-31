"""
Lesson 09: Exercise — Dependency Pre-Flight Checker

Task:
Write a dependency checker function `check_dependencies(required_modules: list) -> bool`:
1. Loop over each module name in `required_modules`.
2. Attempt to import it dynamically using `__import__(name)`.
3. Catch `ModuleNotFoundError` or `ImportError`.
4. Print `[FOUND]` or `[MISSING]` for each module.
5. If any required module is missing, return `False` and print the `pip install` command needed to fix it.
"""

REQUIRED_DEVOPS_MODULES = ["sys", "os", "json", "math", "platform", "requests", "yaml"]

# TODO: Implement dependency pre-flight check function

if __name__ == "__main__":
    pass
