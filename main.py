#!/usr/bin/env python3

from scanner.port_scanner import PortScanner
from utils.menu import display_menu, clear_screen, pause
from tools import ping, traceroute, dns_lookup, whois_lookup, port_check, reverse_lookup, proxy_checker, bandwidth_meter, network_calculator, network_mask_calculator, country_by_ip, unit_converter, exploit_runner
from tools import network_scanner 

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            ip = input("Enter IP address: ")
            ports = input("Enter ports to scan (comma-separated): ")
            ports = [int(port) for port in ports.split(",")]
            PortScanner.active_scan(ip, ports)
            pause()
        elif choice == "2":
            ip = input("Enter IP address: ")
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))
            PortScanner.passive_scan(ip, start_port, end_port)
            pause()
        elif choice == "3":
            ip = input("Enter IP address: ")
            ports = input("Enter ports to scan (comma-separated): ")
            ports = [int(port) for port in ports.split(",")]
            PortScanner.syn_scan(ip, ports)
            pause()
        elif choice == "4":
            ip = input("Enter IP address: ")
            ports = input("Enter ports to scan (comma-separated): ")
            ports = [int(port) for port in ports.split(",")]
            PortScanner.udp_scan(ip, ports)
            pause()
        elif choice == "5":
            ip = input("Enter IP address: ")
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))
            PortScanner.comprehensive_scan(ip, start_port, end_port)
            pause()
        elif choice == "6":
            host = input("Enter host or IP: ")
            ping.ping(host)
            pause()
        elif choice == "7":
            host = input("Enter host or IP: ")
            traceroute.traceroute(host)
            pause()
        elif choice == "8":
            host = input("Enter domain: ")
            dns_lookup.dns_lookup(host)
            pause()
        elif choice == "9":
            host = input("Enter domain or IP: ")
            whois_lookup.whois_lookup(host)
            pause()
        elif choice == "10":
            ip = input("Enter IP address: ")
            port = int(input("Enter port: "))
            port_check.port_check(ip, port)
            pause()
        elif choice == "11":
            ip = input("Enter IP address: ")
            reverse_lookup.reverse_lookup(ip)
            pause()
        elif choice == "12":
            host = input("Enter proxy server address: ")
            proxy_checker.proxy_checker(host)
            pause()
        elif choice == "13":
            bandwidth_meter.bandwidth_meter()
            pause()
        elif choice == "14":
            network = input("Enter network (e.g., 192.168.1.0/24): ")
            network_calculator.network_calculator(network)
            pause()
        elif choice == "15":
            subnet = input("Enter subnet (e.g., 192.168.1.0/255.255.255.0): ")
            network_mask_calculator.network_mask_calculator(subnet)
            pause()
        elif choice == "16":
            ip = input("Enter IP address: ")
            country_by_ip.country_by_ip(ip)
            pause()
        elif choice == "17":
            unit_converter.unit_converter()
            pause()
        elif choice == "18":
            exploit_runner.run_exploit()
            pause()
        elif choice == '19':
            start_ip = input("Enter start IP address (e.g., 10.0.0.1): ")
            end_ip = input("Enter end IP address (e.g., 10.0.0.255): ")
            try:
                network_scanner.scan_network(start_ip, end_ip)
                pause()
            except KeyboardInterrupt:
                print("\nScan cancelled. Returning to main menu.")
                if os.path.isfile('cancel.txt'):
                    os.remove('cancel.txt')
                clear_screen()
        elif choice == '20':
            print("Exiting LJSC. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
