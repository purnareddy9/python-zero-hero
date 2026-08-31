"""
Lesson 03 (Module 05): Solution — Configurable Pipeline Logger
"""
import logging

def create_pipeline_logger(pipeline_name: str, verbose_debug: bool = False) -> logging.Logger:
    logger = logging.getLogger(pipeline_name)
    target_level = logging.DEBUG if verbose_debug else logging.INFO
    logger.setLevel(target_level)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(target_level)
        formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

if __name__ == "__main__":
    print("========================================")
    print("       PIPELINE LOGGER AUDIT TEST       ")
    print("========================================")
    
    print("1. Standard Mode (INFO level):")
    std_logger = create_pipeline_logger("ci-builder", verbose_debug=False)
    std_logger.debug("Debug: Resolving Docker base image dependencies (HIDDEN)")
    std_logger.info("Info: Image compilation started.")
    std_logger.error("Error: Health check probe failed.")
    
    print("\n2. Verbose Mode (DEBUG level enabled):")
    debug_logger = create_pipeline_logger("ci-debug-builder", verbose_debug=True)
    debug_logger.debug("Debug: Resolving Docker base image dependencies (VISIBLE)")
    debug_logger.info("Info: Image compilation started.")
    debug_logger.error("Error: Health check probe failed.")
    print("========================================")
