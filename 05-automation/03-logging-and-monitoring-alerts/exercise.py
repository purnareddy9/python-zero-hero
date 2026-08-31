"""
Lesson 03 (Module 05): Exercise — Configurable Pipeline Logger

Task:
Write a function `create_pipeline_logger(pipeline_name: str, verbose_debug: bool = False)`:
1. Creates and returns a `logging.Logger` instance named `pipeline_name`.
2. Formats messages as: `[LEVEL] %(name)s: %(message)s`.
3. If `verbose_debug == True`, set the logger level to `logging.DEBUG`.
4. If `verbose_debug == False`, set the logger level to `logging.INFO`.
5. Attach a `StreamHandler` if none exist.
6. Test emitting messages at `DEBUG`, `INFO`, and `ERROR` levels.
"""
import logging

# TODO: Implement create_pipeline_logger function

if __name__ == "__main__":
    pass
