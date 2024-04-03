import socket
import ipaddress
import sys

def revDNS(ip):
    print("[#] Performing reverse DNS lookup for IP address: " + ip)
    try:
        result = socket.gethostbyaddr(ip)
        print(f'\033[92mDomain name for {ip} is: {result[0]}\033[0m')
        return result
    except socket.herror:
        print(f'\033[91mCould not look up {ip}\033[0m')
        return None

def process_ip_input(ip_input):
    if '/' in ip_input:
        try:
            network = ipaddress.IPv4Network(ip_input, strict=False)
            for ip in network.hosts():
                revDNS(str(ip))
        except ValueError as e:
            print(f"Error processing IP range: {e}")
    else:
        revDNS(ip_input)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    ip_input = line.strip()
                    if ip_input:
                        process_ip_input(ip_input)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
    else:
        while True:
            ip_input = input('Enter the IP address or range (CIDR notation), or q to quit: ')
            
            if ip_input.lower() == 'q':
                break

            process_ip_input(ip_input)
