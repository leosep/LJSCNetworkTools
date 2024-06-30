import os
import platform
import subprocess
from datetime import datetime
import socket
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = """
 _        _ ____   ____ 
| |      | / ___| / ___|
| |   _  | \___ \| |    
| |__| |_| |___) | |___ 
|_____\___/|____/ \____|
    """
    print(header)
    print("=" * 60)

def scan_network(start_ip, end_ip):
    clear_screen()
    print_header()
    print(f"Scanning network from {start_ip} to {end_ip}...\n")
    
    try:
        start_ip_split = start_ip.split('.')
        end_ip_split = end_ip.split('.')
        
        if len(start_ip_split) != 4 or len(end_ip_split) != 4:
            raise ValueError("Invalid IP address format. Please use format like '10.0.0.1'")
        
        start_octet = int(start_ip_split[3])
        end_octet = int(end_ip_split[3])
        
        if start_ip_split[:3] != end_ip_split[:3]:
            raise ValueError("Start and end IPs must have the same network prefix (e.g., 10.0.0)")
        
        network_prefix = start_ip_split[:3]
        
        for i in range(start_octet, end_octet + 1):
            ip = f"{'.'.join(network_prefix)}.{i}"
            
            # Check for cancellation
            if os.path.isfile('cancel.txt'):
                print("Scan cancelled by user.")
                os.remove('cancel.txt')
                break
            
            response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")  # ICMP ping
            
            if response == 0:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    hostname = "Hostname not found"
                print(f"IP {ip} is UP ({hostname})")
            else:
                print(f"IP {ip} is DOWN")
                
    except ValueError as e:
        print(f"Error: {e}")

    print("\nScan complete.")

if __name__ == "__main__":
    start_ip = input("Enter start IP address (e.g., 10.0.0.1): ")
    end_ip = input("Enter end IP address (e.g., 10.0.0.255): ")
    scan_network(start_ip, end_ip)
