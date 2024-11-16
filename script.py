import nmap
import time
import json
import os

TARGET_IP = "192.168.1.0/24"
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_TIME_FORMAT = "_%Y-%m-%d_%H-%M-%S"
GLOBAL_SCAN_DATE = time.strftime(LOG_TIME_FORMAT, time.localtime(time.time()))

LOG_FOLDER = "logs"
JSON_FOLDER = "json"
LOG_NAME = f"log{GLOBAL_SCAN_DATE}.txt"
JSON_NAME = "hostList"

TIME_BETWEEN_SCANS = 30

host_list = {
    
}

os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(JSON_FOLDER, exist_ok=True)

def run_nmap_scan(IP):
    newHostFound = False
    newHosts = {}
    nm = nmap.PortScanner()
    nm.scan(hosts=IP, arguments="-sn")
    hosts = nm.all_hosts()
    
    print("SCAN")
    print(hosts)

    formated_time = time.strftime(TIME_FORMAT, time.localtime(time.time()))

    for host in hosts:
        
        if not host in host_list:
            newHostFound = True
            print(f"NEW HOST DETECTED")
            
            host_status = nm[host].state()
            host_names = nm[host]['hostnames']
            host_address = nm[host]['addresses']
            
            newHost = {
            "status": host_status,
            "hostnames": nm[host]['hostnames'],
            "address": nm[host]['addresses'],
            "firstDetectionTime": formated_time,
            "lastDetectionTime": formated_time
            }
           
            host_list[host] = newHost
            newHosts[host] = newHost
            
            print(f"Host: {host}")
            print(f"Status: {host_status}")

            if host_status == 'up':
                print(f"Host {host} is up!")
                if host_names:
                    print(f"Hostnames: {host_names}")
                print(f"Address: {host_address}")
                print("-" * 40)
                
        else:
            host_list[host]["lastDetectionTime"] = formated_time
            
    return {"newHostFound": newHostFound, "newHostsList": newHosts}
       
while True:
    scan_status = run_nmap_scan(TARGET_IP)
    
    if scan_status["newHostFound"]:
        
        new_hosts = scan_status["newHostsList"]
        
        with open(f"{LOG_FOLDER}/{LOG_NAME}", "a") as file:
            
            for key in new_hosts:
                new_host = key
                new_host_detectionTimeStamp = new_hosts[key]["firstDetectionTime"]
                new_host_hostnames = new_hosts[key]["hostnames"]
                new_host_address = new_hosts[key]["address"]

                file.write("#"*40+"\n")
                file.write(f"NEW HOST DETECTED\nHost: {new_host}\nDetection Time: {new_host_detectionTimeStamp}\n")
                
                file.write(f"\nHostname:\n") 
                for hostnames in new_hosts[key]["hostnames"]:
                    for hostname in hostnames:
                        file.write(f"{hostname}: {hostnames[hostname]}\n")
                    
                file.write(f"\nAddress:\n")    
                for address in new_host_address:
                    file.write(f"{address}: {new_host_address[address]}\n")
                    
                file.write("#"*40+"\n\n")


    if os.path.exists(f"{JSON_FOLDER}/{JSON_NAME}.json"):
        with open(f"{JSON_FOLDER}/{JSON_NAME}.json", "r") as file:
            data = json.load(file)
    else:
        data = {}
        
    for key in host_list:
        data[key] = host_list[key]

    with open(f"{JSON_FOLDER}/{JSON_NAME}.json", "w") as file:
        json.dump(data, file, indent=4)

    time.sleep(TIME_BETWEEN_SCANS)
    