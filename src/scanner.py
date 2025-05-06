import socket
import threading

PORTS = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open on {target}")
            else:
                print(f"Port {port} is closed on {target}")
    except Exception as e:
        print(f"Error scanning port {port} on {target}: {e}")

def scan_ports(target):
    threads = []
    for port in PORTS:
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()