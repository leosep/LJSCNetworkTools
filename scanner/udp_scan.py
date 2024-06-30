import socket
from scapy.all import IP, UDP, sr1

def udp_scan(ip, ports):
    for port in ports:
        pkt = IP(dst=ip)/UDP(dport=port)
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp is None:
            print(f"Port {port}: Open/Filtered (UDP)")
        elif resp.haslayer(UDP):
            print(f"Port {port}: Open (UDP)")
        else:
            print(f"Port {port}: Closed/Filtered (UDP)")
