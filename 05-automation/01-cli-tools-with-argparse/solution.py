"""
Lesson 01 (Module 05): Solution — Disk Audit CLI Tool
"""
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="disk-audit-cli",
        description="💾 Production Filesystem Threshold & Audit Tool"
    )
    
    parser.add_argument(
        "-m", "--mount",
        required=True,
        help="Target filesystem mount point (e.g. /, /data, /var/log)"
    )
    
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=85,
        help="Percentage capacity warning threshold (default: 85)"
    )
    
    parser.add_argument(
        "--notify",
        action="store_true",
        help="Dispatch notification alert if threshold breached"
    )
    
    args = parser.parse_args()
    
    print("========================================")
    print("        DISK AUDIT CLI EXECUTION        ")
    print("========================================")
    print(f"Target Mount     : {args.mount}")
    print(f"Alert Threshold  : {args.threshold}%")
    print(f"Notification Mode: {args.notify}")
    print("----------------------------------------")
    
    if args.threshold >= 90:
        print("[CRITICAL WARNING] High threshold (> 90%) configured!")
        
    if args.notify:
        print("[ALERT] Notification dispatched to on-call channel.")
    else:
        print("[INFO] Standalone local execution (no alerts dispatched).")
        
    print("========================================")

if __name__ == "__main__":
    main()
