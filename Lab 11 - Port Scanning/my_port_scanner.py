import socket
import sys
import time

def scan_port(target_ip, target_port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a TCP socket
        sock.settimeout(1)  # Set a timeout for the socket connection
        
        # Try to connect to the target IP and port
        result = sock.connect_ex((target_ip, target_port)) # try to connect
        
        if result == 0:
            # Connection successful, target port is open
            print(f"Port {target_port} on {target_ip} is open.")
        elif result == 111  or result == 10061:
            # Connection refused, target port is closed but reachable
            print(f"Port {target_port} on {target_ip} is closed, but not blocked by firewall.")
        else:
            # No response, likely blocked by firewall
            print(f"Port {target_port} on {target_ip} is filtered (possibly blocked by firewall).")
            
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    # Check if IP and port are provided
    if len(sys.argv) != 3:
        print("Usage: python my_port_scanner.py <target_ip> <target_port>")
        sys.exit(1)
    
    # Read IP and port from command line arguments
    target_ip = sys.argv[1]
    print("First input", target_ip)
    target_port = int(sys.argv[2])
    
    # Run the port scan
    scan_port(target_ip, target_port)
