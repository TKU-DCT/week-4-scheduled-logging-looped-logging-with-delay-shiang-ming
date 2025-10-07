import psutil
from datetime import datetime
import csv
import os
import time

def ensure_csv_with_header():
    
    if not os.path.exists("log.csv"):
        with open("log.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])

def get_system_row():
   
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return [now, cpu, memory, disk]

def append_row(row):
    
    with open("log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

if __name__ == "__main__":
    ensure_csv_with_header()  
    for i in range(5):  
        row = get_system_row()
        print("Logged:", row)
        append_row(row)
        if i < 4:  
            time.sleep(10)
