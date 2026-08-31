"""
Lesson 05 (Module 03): Exercise — Regional Server Filter & CSV Exporter

Task:
You are given a raw CSV string of data center nodes:
`raw_csv_data = '''hostname,ip,region,tier
web-01,10.0.1.10,us-east-1,frontend
web-02,10.0.2.10,eu-west-1,frontend
db-01,10.0.1.20,us-east-1,database
cache-01,10.0.3.10,ap-south-1,caching
web-03,10.0.1.11,us-east-1,frontend
'''`

Write a script that:
1. Parses the CSV using `csv.DictReader(io.StringIO(raw_csv_data))`.
2. Filters out all servers belonging to `"us-east-1"`.
3. Writes only the filtered servers to `us_east_inventory.csv` using `csv.DictWriter`.
4. Prints the filtered rows to stdout.
"""
import csv
import io

# TODO: Implement regional CSV filter and exporter

if __name__ == "__main__":
    pass
