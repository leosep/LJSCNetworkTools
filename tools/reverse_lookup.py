import socket

def reverse_lookup(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f"IP {ip} resolves to {host[0]}")
    except socket.herror:
        print(f"Reverse lookup failed for {ip}")
