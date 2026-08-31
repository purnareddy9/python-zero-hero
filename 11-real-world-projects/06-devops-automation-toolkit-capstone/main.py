"""
Capstone Project: DevOps Automation Toolkit CLI
Central entrypoint and subcommand dispatcher.
"""
import argparse
import sys

from health import run_health_check
from disk import run_disk_audit
from logs import run_log_analysis
from docker_ops import run_docker_audit
from k8s_ops import run_k8s_audit
from aws_ops import run_aws_audit

def main():
    parser = argparse.ArgumentParser(
        prog="devops",
        description="🛠️ Production DevOps Automation & SRE Toolkit CLI",
        epilog="Use 'devops <subcommand> --help' for specific command options."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # 1. Health Command
    sub_health = subparsers.add_parser("health", help="Audit host CPU, memory, uptime, and load")
    sub_health.add_argument("--json", action="store_true", help="Output in structured JSON format")
    
    # 2. Disk Command
    sub_disk = subparsers.add_parser("disk", help="Audit filesystem partitions and disk space")
    sub_disk.add_argument("-t", "--threshold", type=float, default=80.0, help="Capacity warning threshold % (default: 80.0)")
    
    # 3. Logs Command
    sub_logs = subparsers.add_parser("logs", help="Stream and analyze application log files")
    sub_logs.add_argument("-f", "--file", default="sample.log", help="Target log file path")
    sub_logs.add_argument("--top", type=int, default=3, help="Top N error causes to display")
    
    # 4. Docker Command
    sub_docker = subparsers.add_parser("docker", help="Inspect container fleet and prune stale resources")
    sub_docker.add_argument("--prune", action="store_true", help="Prune stopped containers and dangling images")
    
    # 5. K8s Command
    sub_k8s = subparsers.add_parser("k8s", help="Audit Kubernetes pods, nodes, and crash loops")
    sub_k8s.add_argument("-n", "--namespace", default="all", help="Target namespace or 'all'")
    
    # 6. AWS Command
    sub_aws = subparsers.add_parser("aws", help="Audit AWS cloud resources, EBS volumes, and spend")
    sub_aws.add_argument("-r", "--region", default="us-east-1", help="Target AWS region (default: us-east-1)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
        
    if args.command == "health":
        run_health_check(as_json=args.json)
    elif args.command == "disk":
        run_disk_audit(threshold=args.threshold)
    elif args.command == "logs":
        run_log_analysis(filepath=args.file, top_n=args.top)
    elif args.command == "docker":
        run_docker_audit(do_prune=args.prune)
    elif args.command == "k8s":
        run_k8s_audit(namespace=args.namespace)
    elif args.command == "aws":
        run_aws_audit(region=args.region)

if __name__ == "__main__":
    main()
