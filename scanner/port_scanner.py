from .active_scan import active_scan
from .passive_scan import passive_scan
from .syn_scan import syn_scan
from .udp_scan import udp_scan
from .comprehensive_scan import comprehensive_scan

class PortScanner:
    @staticmethod
    def active_scan(ip, ports):
        active_scan(ip, ports)

    @staticmethod
    def passive_scan(ip, start_port, end_port):
        passive_scan(ip, start_port, end_port)

    @staticmethod
    def syn_scan(ip, ports):
        syn_scan(ip, ports)

    @staticmethod
    def udp_scan(ip, ports):
        udp_scan(ip, ports)

    @staticmethod
    def comprehensive_scan(ip, start_port, end_port):
        comprehensive_scan(ip, start_port, end_port)
