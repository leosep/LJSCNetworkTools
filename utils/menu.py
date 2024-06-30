import os
import datetime

# Define the version number
VERSION = "1.0"

def display_menu():
    clear_screen()
    print_header()
    print("1. Active Scan (TCP Connect)")
    print("2. Passive Scan (TCP Connect)")
    print("3. SYN Scan")
    print("4. UDP Scan")
    print("5. Comprehensive Scan (TCP and UDP)")
    print("6. Ping")
    print("7. Traceroute")
    print("8. DNS Lookup")
    print("9. WHOIS Lookup")
    print("10. Port Check")
    print("11. Reverse Lookup")
    print("12. Proxy Checker")
    print("13. Bandwidth Meter")
    print("14. Network Calculator")
    print("15. Network Mask Calculator")
    print("16. Country by IP")
    print("17. Network and Computer Unit Converter")
    print("18. Run Exploit")
    print("19. Network Scanner")  # Option for Network Scanner
    print("20. Exit")

def print_header():
    header = """
 _        _ ____   ____ 
| |      | / ___| / ___|
| |   _  | \___ \| |    
| |__| |_| |___) | |___ 
|_____\___/|____/ \____|
Version: {}
    """.format(VERSION)
    print(header)
    print(f"Author: Leandro Sepulveda")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 60)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Press any key to continue...")
    clear_screen()
