from .active_scan import scan_port as tcp_scan_port
from .udp_scan import udp_scan
from threading import Thread, Lock
from queue import Queue

print_lock = Lock()

def threader(q, ip):
    while True:
        worker = q.get()
        tcp_scan_port(ip, worker)
        q.task_done()

def comprehensive_scan(ip, start_port, end_port):
    q = Queue()
    num_threads = 50

    for _ in range(num_threads):
        t = Thread(target=threader, args=(q, ip))
        t.daemon = True
        t.start()

    for port in range(start_port, end_port + 1):
        q.put(port)

    q.join()

    # Run UDP scan after TCP scan completes
    udp_ports = list(range(start_port, end_port + 1))
    udp_scan(ip, udp_ports)
