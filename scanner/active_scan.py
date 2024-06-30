import socket
from threading import Lock

print_lock = Lock()

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        with print_lock:
            print(f"Port {port}: Open (TCP Connect)")
        scanner.close()
    except:
        pass

def active_scan(ip, ports):
    for port in ports:
        scan_port(ip, port)
