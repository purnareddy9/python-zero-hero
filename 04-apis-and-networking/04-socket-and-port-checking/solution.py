"""
Lesson 04 (Module 04): Solution — Database Readiness Probe
"""
import socket
import time

def wait_for_service_port(host: str, port: int, timeout_sec: int = 5, probe_interval_sec: float = 1.0) -> bool:
    print("========================================")
    print("     TCP SERVICE READINESS PROBE        ")
    print("========================================")
    print(f"Target Service: {host}:{port} (Max Timeout: {timeout_sec}s)\n")
    
    start_time = time.time()
    attempt = 1
    
    while (time.time() - start_time) < timeout_sec:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1.0)
            status = sock.connect_ex((host, port))
            
            elapsed = round(time.time() - start_time, 1)
            if status == 0:
                print(f"[+] [Probe #{attempt} @ {elapsed}s] Service {host}:{port} is OPEN & READY!")
                print("========================================")
                return True
            else:
                print(f"[*] [Probe #{attempt} @ {elapsed}s] Port closed / not listening yet. Retrying...")
                
        attempt += 1
        time.sleep(probe_interval_sec)
        
    print(f"\n[!] TIMEOUT ERROR: Service {host}:{port} failed to start within {timeout_sec} seconds.")
    print("========================================")
    return False

if __name__ == "__main__":
    # Test with public DNS port 53 (should succeed immediately)
    wait_for_service_port("8.8.8.8", 53, timeout_sec=3)
