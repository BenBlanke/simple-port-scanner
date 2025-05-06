import socket
from scanner import scan_ports

def main():
    try:
        target = input("Enter the target IP address or hostname to scan: ").strip()
        try:
            socket.inet_aton(target)
        except socket.error:
            print(f"Invalid IP address format: {target}")
            return
        
        print(f"[*] Starting port scan on {target}...")
        scan_ports(target)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()