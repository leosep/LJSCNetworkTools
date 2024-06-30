import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Domain {domain} has IP: {ip}")
    except socket.gaierror:
        print(f"DNS lookup failed for {domain}")
