"""
Lesson 05 (Module 03): Solution — Regional Server Filter & CSV Exporter
"""
import csv
import io
import os

raw_csv_data = """hostname,ip,region,tier
web-01,10.0.1.10,us-east-1,frontend
web-02,10.0.2.10,eu-west-1,frontend
db-01,10.0.1.20,us-east-1,database
cache-01,10.0.3.10,ap-south-1,caching
web-03,10.0.1.11,us-east-1,frontend
"""

def filter_and_export_servers(raw_csv, target_region="us-east-1", output_csv="us_east_inventory.csv"):
    reader = csv.DictReader(io.StringIO(raw_csv.strip()))
    
    filtered_rows = []
    for row in reader:
        if row["region"] == target_region:
            filtered_rows.append(row)
            
    if filtered_rows:
        fieldnames = list(filtered_rows[0].keys())
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_rows)
            
    print("========================================")
    print(f"   REGIONAL INVENTORY: [{target_region}]")
    print("========================================")
    print(f"Total Matches Found: {len(filtered_rows)}\n")
    for r in filtered_rows:
        print(f"  - Host: {r['hostname']:<10} | IP: {r['ip']:<12} | Tier: {r['tier']}")
        
    print(f"\n[+] Exported to '{os.path.abspath(output_csv)}'")
    print("========================================")

if __name__ == "__main__":
    filter_and_export_servers(raw_csv_data, target_region="us-east-1")
