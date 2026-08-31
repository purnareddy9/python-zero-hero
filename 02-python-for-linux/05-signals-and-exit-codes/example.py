"""
Lesson 05 (Module 02): Signals, Graceful Shutdowns, and Exit Codes
Example Script: Resilient Worker Daemon with Graceful SIGTERM/SIGINT Handler
"""
import signal
import sys
import time
import os

class BackgroundQueueWorker:
    def __init__(self):
        self.is_running = True
        self.processed_items = 0
        
        # Register signal handlers
        signal.signal(signal.SIGINT, self.shutdown_handler)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, self.shutdown_handler)
            
    def write_pid(self):
        print(f"[*] Worker PID: {os.getpid()}")
        
    def shutdown_handler(self, signum, frame):
        sig_name = "SIGINT (Ctrl+C)" if signum == signal.SIGINT else f"SIGTERM ({signum})"
        print(f"\n[!] Signal received: {sig_name}")
        print("[*] Initiating graceful drain and cleanup sequence...")
        
        self.is_running = False
        print(f"[+] Processed {self.processed_items} items before shutdown.")
        print("[+] Orderly shutdown complete. Exiting cleanly (code 0).")
        sys.exit(0)
        
    def run(self, max_iterations=5):
        self.write_pid()
        print("[*] Worker active. Processing queue events...")
        
        for i in range(1, max_iterations + 1):
            if not self.is_running:
                break
            print(f"    -> Processed batch event #{i}")
            self.processed_items += 1
            time.sleep(0.5)
            
        print("[+] Batch processing finished naturally.")

if __name__ == "__main__":
    worker = BackgroundQueueWorker()
    worker.run(max_iterations=4)
