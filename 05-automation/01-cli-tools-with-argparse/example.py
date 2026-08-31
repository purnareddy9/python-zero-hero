"""
Lesson 01 (Module 05): Building Professional CLI Automation Tools with argparse
Example Script: Multi-Environment Deployment & Maintenance CLI Tool
"""
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="devops-deployer",
        description="🚀 Enterprise Multi-Cloud Deployment & Automation CLI",
        epilog="Example: python example.py payment-service --env production --replicas 5 --dry-run"
    )
    
    parser.add_argument("service_name", help="Name of the service / container to manage")
    
    parser.add_argument(
        "-e", "--env",
        choices=["development", "staging", "production"],
        default="staging",
        help="Target cloud deployment environment (default: staging)"
    )
    
    parser.add_argument(
        "-r", "--replicas",
        type=int,
        default=2,
        help="Number of container replicas to launch (default: 2)"
    )
    
    parser.add_argument(
        "--image-tag",
        default="v1.0.0",
        help="Docker image version tag (default: v1.0.0)"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate execution without modifying real infrastructure"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose debug logging output"
    )
    
    args = parser.parse_args()
    
    print("========================================")
    print("      DEVOPS DEPLOYMENT CLI EXECUTION   ")
    print("========================================")
    print(f"Target Service   : {args.service_name}")
    print(f"Environment      : {args.env}")
    print(f"Image Version    : {args.image_tag}")
    print(f"Desired Replicas : {args.replicas}")
    print(f"Dry-Run Mode     : {args.dry_run}")
    print(f"Verbose Logging  : {args.verbose}")
    print("----------------------------------------")
    
    if args.dry_run:
        print("[DRY-RUN] [SIMULATION ONLY] Plan: Would launch", args.replicas, "replicas of", args.service_name)
        print("[DRY-RUN] No infrastructure modified.")
    else:
        print(f"[ACTION] Applying Kubernetes deployment manifests for '{args.service_name}'...")
        print("[+] Deployment completed successfully.")
        
    print("========================================")

if __name__ == "__main__":
    main()
