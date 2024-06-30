import ipaddress

def network_mask_calculator(subnet):
    network, netmask = subnet.split('/')
    net = ipaddress.ip_network(f"{network}/{netmask}", strict=False)
    print(f"Network: {net.network_address}")
    print(f"Netmask: {net.netmask}")
    print(f"Broadcast: {net.broadcast_address}")
    print(f"Host range: {net[1]} - {net[-2]}")
    print(f"Number of hosts: {net.num_addresses - 2}")
