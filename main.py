import psutil
from datetime import datetime
import csv
import os
import time

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # TODO: Get CPU, memory, and disk usage using psutil
    cpu = 
    memory = 
    disk = 
    
    return [now, cpu, memory, disk]

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])
        writer.writerow(data)

if __name__ == "__main__":
    # TODO: Repeat the log process 5 times with 10-second intervals
    pass
