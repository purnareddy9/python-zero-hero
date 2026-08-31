"""
Lesson 05 (Module 02): Solution — Graceful Metrics Aggregator
"""
import signal
import sys
import time

class MetricsCollector:
    def __init__(self):
        self.start_time = time.time()
        self.samples_collected = 0
        
        # Register SIGINT and SIGTERM
        signal.signal(signal.SIGINT, self.graceful_exit)
        if hasattr(signal, "SIGTERM"):
            signal.signal(signal.SIGTERM, self.graceful_exit)
            
    def graceful_exit(self, signum, frame):
        elapsed = round(time.time() - self.start_time, 2)
        print("\n========================================")
        print("       METRICS COLLECTOR SHUTDOWN       ")
        print("========================================")
        print(f"[+] Signal caught: {signum}")
        print(f"[+] Total Samples Captured: {self.samples_collected}")
        print(f"[+] Total Runtime: {elapsed} seconds")
        print("[+] Buffer flushed to storage.")
        print("[+] Exiting with status code 0 (Success).")
        print("========================================")
        sys.exit(0)
        
    def start_collection(self, max_samples=3):
        print("========================================")
        print("       METRICS COLLECTOR ACTIVE         ")
        print("========================================")
        print("[*] Collector running. Emitting probes...")
        
        for i in range(1, max_samples + 1):
            self.samples_collected += 1
            print(f"    [Probe {i}] CPU: 24.1% | RAM: 58.2% | Time: {time.strftime('%H:%M:%S')}")
            time.sleep(0.5)
            
        # Simulate natural completion
        self.graceful_exit(0, None)

if __name__ == "__main__":
    collector = MetricsCollector()
    collector.start_collection(max_samples=3)
