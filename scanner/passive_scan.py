import socket
from threading import Thread, Lock
from queue import Queue

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

def threader(q, ip):
    while True:
        worker = q.get()
        scan_port(ip, worker)
        q.task_done()

def passive_scan(ip, start_port, end_port):
    q = Queue()
    num_threads = 50

    for _ in range(num_threads):
        t = Thread(target=threader, args=(q, ip))
        t.daemon = True
        t.start()

    for port in range(start_port, end_port + 1):
        q.put(port)

    q.join()
