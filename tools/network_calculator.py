import ipaddress

def network_calculator(network):
    net = ipaddress.ip_network(network, strict=False)
    print(f"Network: {net.network_address}")
    print(f"Netmask: {net.netmask}")
    print(f"Broadcast: {net.broadcast_address}")
    print(f"Host range: {net[1]} - {net[-2]}")
    print(f"Number of hosts: {net.num_addresses - 2}")
