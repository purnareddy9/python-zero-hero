"""
Lesson 03 (Module 05): Production Logging vs print()
Example Script: Enterprise Multi-Handler Rotating Logging System
"""
import logging
from logging.handlers import RotatingFileHandler

def setup_production_logger(logger_name="devops-engine", log_file="automation.log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger
        
    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(name)s] [PID:%(process)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # 1. Console Handler (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    # 2. Rotating File Handler
    file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    
    return logger

def run_backup_pipeline():
    logger = setup_production_logger()
    
    logger.info("Starting automated database snapshot pipeline...")
    logger.debug("Connecting to target RDS instance at endpoint: rds-primary.internal:5432")
    
    db_storage_used_pct = 82.5
    if db_storage_used_pct > 80.0:
        logger.warning(f"Database storage threshold warning: {db_storage_used_pct}% utilized.")
        
    logger.error("Snapshot replica synchronization experienced 1 retry attempt.")
    logger.info("Snapshot pipeline execution concluded.")

if __name__ == "__main__":
    run_backup_pipeline()
