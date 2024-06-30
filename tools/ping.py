import os

def ping(host):
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is not reachable")
