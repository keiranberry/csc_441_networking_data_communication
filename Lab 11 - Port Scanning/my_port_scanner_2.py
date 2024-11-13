import socket
import sys
import errno

def scan_port(target_ip, target_port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP socket
        sock.settimeout(1)  # Set a timeout for the socket connection
        
        # Try to connect to the target IP and port
        result = sock.connect_ex((target_ip, target_port))  # attempt to connect
        
        if result == 0:
            print(f"Port {target_port} on {target_ip} is open.")
        elif result == errno.ECONNREFUSED:
            print(f"Port {target_port} on {target_ip} is closed.")
        elif result == errno.ETIMEDOUT:
            print(f"Port {target_port} on {target_ip} is filtered or unreachable (timeout).")
        elif result == errno.ENETUNREACH:
            print(f"Network is unreachable for port {target_port} on {target_ip}.")
        elif result == errno.EHOSTUNREACH:
            print(f"No route to host for port {target_port} on {target_ip}.")
        elif result == errno.EADDRNOTAVAIL:
            print(f"Invalid address: {target_ip}.")
        else:
            print(f"Port {target_port} on {target_ip} returned error code: {result}.")
            
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sock.close()

def parse_ports(port_arg):
    ports = set() # no duplicates
    ranges = port_arg.split(',')
    
    for r in ranges:
        if '-' in r:
            start, end = map(int, r.split('-'))
            ports.update(range(start, end + 1))
        else:
            ports.add(int(r))
    
    return ports
if __name__ == "__main__":
    # Check if IP and port arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python my_port_scanner.py <target_ip> <target_ports>")
        sys.exit(1)
    
    # Read IP and port from command line arguments
    target_ip = sys.argv[1]
    target_ports_arg = sys.argv[2]
    
    # parse ports to handle multiple
    target_ports = parse_ports(target_ports_arg)
    
    # Run the port scan for each port
    for port in target_ports:
        scan_port(target_ip, port)
