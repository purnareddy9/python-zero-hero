"""
Lesson 07: Loops (for, while, break, continue)
Example Script: Deployment Readiness Polling & Server Fleet Health Checker
"""
import time

def simulate_service_polling(max_retries=4, delay_seconds=1):
    print("========================================")
    print("   DEPLOYMENT STATUS POLLING SERVICE    ")
    print("========================================")
    
    # Simulate service transitioning from PENDING -> INITIALIZING -> READY
    mock_status_sequence = ["PENDING", "PENDING", "INITIALIZING", "READY"]
    
    attempt = 1
    is_ready = False
    
    while attempt <= max_retries:
        current_status = mock_status_sequence[attempt - 1]
        print(f"[*] [Attempt {attempt}/{max_retries}] Checking service readiness... Status: {current_status}")
        
        if current_status == "READY":
            print("[+] Service is READY! Traffic routing enabled.")
            is_ready = True
            break
            
        print(f"    Waiting {delay_seconds}s before next probe...")
        time.sleep(delay_seconds)
        attempt += 1
        
    if not is_ready:
        print("[!] TIMEOUT ERROR: Service failed to reach READY state within threshold.")
        return False
        
    print("========================================")
    return True

if __name__ == "__main__":
    simulate_service_polling()
