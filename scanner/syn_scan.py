import socket
from scapy.all import IP, TCP, sr1

def syn_scan(ip, ports):
    for port in ports:
        pkt = IP(dst=ip)/TCP(dport=port, flags='S')
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:
            print(f"Port {port}: Open (SYN)")
        else:
            print(f"Port {port}: Closed/Filtered (SYN)")
